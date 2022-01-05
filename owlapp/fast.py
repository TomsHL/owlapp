from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from owlapp import translation, database_functions as dbf, slack_functions as sf
from pydantic import BaseModel
from typing import Optional

import datetime
import json
import uvicorn

''' API for the Owlint technical test.
    - 1st endpoint : root, for pinging API and checking availability.
    - 2nd endpoint (POST) : check the language of a comment, translate in the
    opposite language (EN<->FR), add the comment (original and translated) in a
    database (see owlappdb), post the original comment on a Slack channel.
    - 3nd endpoint : retrieve all comments on a channel attached to a target.
'''

#  Instantiate FastAPI app, manage CORS (allow all connections)
app = FastAPI(title="Owlapp")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define Item (pydantic method)
class Item(BaseModel):
    text_new_comment: Optional[str] = None
    textFr: Optional[str] = None
    textEn: Optional[str] = None
    publishedAt: float = datetime.datetime.now().timestamp()
    authorId: str
    targetId: str


# Root method
@app.get("/")
def index():
    return  {"greeting": "Status UP"}


# POST endpoint to add a new comment on an object
@app.post("/new_comment")
def post_comment(item: Item):

    # Detect language of the comment
    source_lang = translation.detect_language(item.text_new_comment)

    '''Translate comment (If comment is neither En nor Fr, raise error),
        send back a dict with the response'''
    # Language detection , translation
    if source_lang == 'en':
        translated = translation.translate_text('fr', item.text_new_comment)
        resp = {
            'textFr': translated,
            'textEn': item.text_new_comment,
            'publishedAt': item.publishedAt,
            'authorId': item.authorId,
            'targetId': item.targetId
        }
        # Insertion in the database
        dbf.insert_comment(resp['targetId'], resp['textFr'], resp['textEn'],
                           resp['publishedAt'], resp['authorId'])

        # Post the comment on Slack
        sf.post_message(item.authorId, item.targetId, translated,
                        item.text_new_comment)

        # Returning the result to the request
        return json.dumps(resp)

    elif source_lang == 'fr':
        translated = translation.translate_text('en', item.text_new_comment)
        resp = {
            'targetId': item.targetId,
            'textFr': item.text_new_comment,
            'textEn': translated,
            'publishedAt': item.publishedAt,
            'authorId': item.authorId
        }
        # Insertion in the database
        dbf.insert_comment(resp['targetId'], resp['textFr'], resp['textEn'],
                           resp['publishedAt'], resp['authorId'])

        # Post the comment on Slack
        sf.post_message(item.authorId, item.targetId, item.text_new_comment,
                        translated)

        # Returning the result to the request
        return json.dumps(resp)
    else:
        # Error if source language is neither EN nor FR
        raise HTTPException(status_code=404,
                            detail="Source language is not Fr or En")


# retrieve all comments on the channel matching a target ID
@app.get("/get_comments")
def enpoint_get_comments(targetId):
    comments = dbf.get_comments(targetId)
    return comments


if __name__ == '__main__':
    uvicorn.run("fast:app",
                host="127.0.0.1",
                port=8080,
                log_level="debug",
                reload="true")
