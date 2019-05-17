from flask import Flask,request


app = Flask(__name__)



@app.route("/callback", methods=["POST"])
def hello_slack():
    """Example Incoming Data - application/x-www-form-urlencoded
    token=gIkuvaNzQIHg97ATvDxqgjtO
    team_id=T0001
    team_domain=example
    enterprise_id=E0001
    enterprise_name=Globular%20Construct%20Inc
    channel_id=C2147483705
    channel_name=test
    user_id=U2147483697
    user_name=Steve
    command=/weather
    text=94070
    response_url=https://hooks.slack.com/commands/1234/5678
    trigger_id=13345224609.738474920.8088930838d88f008e0
    """
    print(request.form)
    return f"""For every Data Scientists, let's express your abilities into the world of software development.
You will learn many things including.\n
    - Advanced Python Topics\n
        - Object Oriented Programing\n
        - Python Decorators\n
        - Meta Programing\n
    - Bacnkend Web API\n
    - Documentation\n
    - Unit Testing\n
    - CI/CI\n
    - Security\n
Join this group and have fun!
"""

if __name__ == "__main__":
    app.run()