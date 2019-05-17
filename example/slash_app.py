import os

from flask import Flask,request

from slacksdk.verify import verify

app = Flask(__name__)

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

@app.route("/callback", methods=["POST"])
def hello_slack():
    if verify(SLACK_SIGNING_SECRET,request):
        return f"""For every Data Scientists, let's express your abilities into the world of software development.
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
    else:
        return "You are not verified"

if __name__ == "__main__":
    app.run()