from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from owlapp import translation
from typing import Optional

import datetime

#  Instantiate app, manage CORS (allow all connections), define item
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    text_new_comment : Optional[str] = None
    textFr: Optional[str] = None
    textEn: Optional[str] = None
    publishedAt: float = datetime.datetime.now().timestamp()
    authorId: str
    targetId: str

# Root method
@app.get("/")
def index():
    return {"greeting": "Status OK"}

# POST endpoint to add a new comment on an object
@app.post("/new_comment")
def post_comment(item: Item):
    source_lang = translation.detect_language(item.text_new_comment)
    if source_lang == 'en':
        return translation.translate_text('fr', item.text_new_comment)
    elif source_lang == 'fr':
        return translation.translate_text('en', item.text_new_comment)
    else:
        raise HTTPException(status_code=404, detail="Source language is not Fr or En")
