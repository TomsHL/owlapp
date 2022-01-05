from slack import WebClient
from dotenv import load_dotenv

import os

load_dotenv()

def post_message(authorId, targetId, textFr, textEn):
    '''Posts a message and its translation on a Slack channel.
    Slack variables as token and channel are defined in the .env file
    '''

    # Create the payload
    ID_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ('Comment from : ' + authorId + ', target : ' + targetId),
        },
    }

    EN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ("EN:\n" + textEn),
        },
    }

    FR_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ("FR:\n" + textFr),
        },
    }

    payload = {
        "channel": os.getenv("SLACK_CHANNEL"),
        "blocks": [
            ID_BLOCK,
            EN_BLOCK,
            FR_BLOCK,
        ],
    }

    # instantiate Slack client
    slack_client = WebClient(token=os.getenv("SLACK_TOKEN"))
    slack_client.chat_postMessage(**payload)

if __name__ == '__main__':
    post_message('Tom', 'Profil_5589', 'Bonjour', 'Hello')
