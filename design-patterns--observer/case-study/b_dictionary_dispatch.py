import time
from flask import Flask, request

app = Flask(__name__)


def time_handler(data):
    return f"Current time is `{time.strftime('%X')}`"


def date_handler(data):
    return f"Today's Date: `{time.strftime('%x')}`"


def echo_handler(data):
    text_to_echo = data["command_data"]
    return " ".join(text_to_echo)


slash_command_dispatcher = {
    "time": time_handler,
    "date": date_handler,
    "echo": echo_handler,
}


@app.route("/", methods=["POST"])
def handle_slash_command():
    command_text = request.form["text"]
    subcommand = command_text.split(" ")[0].lower()
    data = {"command_data": command_text.split(" ")[1:]}

    if subcommand in slash_command_dispatcher:
        return slash_command_dispatcher[subcommand](data)
    return "`unknown command`"
