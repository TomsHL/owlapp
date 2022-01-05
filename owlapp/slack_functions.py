from slack import WebClient
import os

# instantiate Slack client
slack_client = WebClient(token=os.environ.get("SLACK_TOKEN"))
