import time
from flask import Flask, request


class EventEmitterException(Exception):
    pass


class EventAlreadyRegistered(EventEmitterException):
    pass


class EventNotRegistered(EventEmitterException):
    pass


class EventEmitter:
    def __init__(self):
        self.registered_events = {}

    def on(self, event, func=None):
        """Pass in a function or use as a decorator"""
        if event in self.registered_events:
            raise EventAlreadyRegistered(f"{event} already registered")

        def _on(f):
            self.registered_events[event] = f
            return f

        if func is None:
            return _on
        else:
            return _on(func)

    def emit(self, _event, *args, default=None, **kwargs):
        if _event not in self.registered_events:
            if not default:
                raise EventNotRegistered(f"{_event} has not been registered")
            _event = default

        func = self.registered_events[_event]
        return func(*args, **kwargs)


app = Flask(__name__)
slash_command_emitter = EventEmitter()


@app.route("/", methods=["POST"])
def handle_slash_command():
    command_text = request.form["text"]

    command = command_text.split(" ")[0].lower()
    data = {"command_data": command_text.split(" ")[1:]}
    return slash_command_emitter.emit(command, default="unknown", data=data)


@slash_command_emitter.on("time")
def time_handler(data):
    return f"Current time is `{time.strftime('%X')}`"


@slash_command_emitter.on("date")
def date_handler(data):
    return f"Today's Date: `{time.strftime('%x')}`"


@slash_command_emitter.on("echo")
def echo_handler(data):
    text_to_echo = data["command_data"]
    return " ".join(text_to_echo)


@slash_command_emitter.on("unknown")
def unknown_handler(data):
    return "`unknown command`"
