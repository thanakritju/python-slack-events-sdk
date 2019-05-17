import os 

import requests


BOT_USER_OAUTH_ACCESS_TOKEN = os.getenv("BOT_USER_OAUTH_ACCESS_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

message_payload = {
  "channel": CHANNEL_ID,
  "text": """For every Data Scientists, let's express your abilities into the world of software development.
You will learn many things including.\n
    - Advanced Python Topics\n
        - Object Oriented Programing\n
        - Python Decorators\n
        - Meta Programing\n
    - Backend Web API\n
    - Documentation\n
    - Unit Testing\n
    - CI/CD\n
    - Security\n
Join this group and have fun!
"""
}
response = requests.post(
    "https://slack.com/api/chat.postMessage",
    json = message_payload,
    headers = {"Authorization": f"Bearer {BOT_USER_OAUTH_ACCESS_TOKEN}"}
    )
print(response.json())