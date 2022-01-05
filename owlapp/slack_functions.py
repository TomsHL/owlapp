from slack import WebClient
from dotenv import load_dotenv
import os

load_dotenv()
'''Post a message on Slack with text and info. Variables like Slack channel and
Slack token defined in the .env file'''


def post_message(authorId, targetId, textFr, textEn):

    ID_BLOCK = {
        "type": "section",
        "text": {
            "type":
            "mrkdwn",
            "text":
            ('Comment from : ' + authorId + ', target : ' + targetId + '\n'),
        },
    }

    FR_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ('FR : ' + textFr + '\n'),
        },
    }

    EN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ('EN : ' + textEn + '\n'),
        },
    }

    payload = {
        "channel": os.getenv("SLACK_CHANNEL"),
        "blocks": [
            ID_BLOCK,
            FR_BLOCK,
            EN_BLOCK,
        ],
    }

    # instantiate Slack client
    slack_client = WebClient(token=os.getenv("SLACK_TOKEN"))
    slack_client.chat_postMessage(**payload)

if __name__ == '__main__':
    post_message('Tom', 'This_other_comment', 'Bonjour, test', 'Hello, test')
