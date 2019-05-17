import os

from flask import Flask,request,jsonify

from slacksdk.verify import verify

app = Flask(__name__)

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

@app.route("/callback", methods=["POST"])
def hello_slack():
    if verify(SLACK_SIGNING_SECRET,request):
        return jsonify({
            "response_type": "in_channel",
            "text": f"Hello {request.form['user_name']}",
            "attachments": [
                {
                    "text":f"You entered: {request.form['text']}"
                },
            ],
        })

    else:
        return "You are not verified"

if __name__ == "__main__":
    app.run()