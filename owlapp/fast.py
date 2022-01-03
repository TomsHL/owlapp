from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import datetime

#  Instantiate app, manage CORS
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Item(BaseModel):
    textFr: str
    textEn: str
    publishedAt: datetime.datetime.now().timestamp()
    authorId: str
    targetId: str



# Root method
@app.get("/")
def index():
    return {"greeting": "Status OK"}

# POST endpoint to add a comment on an object
@app.post("/predict")
def post_comment(item: Item):
    # get mix params
    mix_params = {
        'taste': item.taste,
        'appearance': item.appearance,
        'palate': item.palate,
        'aroma': item.aroma,
        'overall': item.overall,
        'content': item.content
    }
