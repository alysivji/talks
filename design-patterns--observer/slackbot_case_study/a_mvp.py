import time

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handle_slash_command():
    command_text = request.form["text"]
    subcommand = command_text.split(" ")[0].lower()
    subcommand_details = command_text.split(" ")[1:]

    if subcommand == "time":
        return f"Current time is `{time.strftime('%X')}`"
    elif subcommand == "date":
        return f"Today's Date: `{time.strftime('%x')}`"
    elif subcommand == "echo":
        return " ".join(subcommand_details)
    elif subcommand == "...":
        # get data requested from database or via API
        ...
    return "`unknown command`"
