from flask import Flask
from middleware import RequestUuidMiddleware


app = Flask(__name__)
app.wsgi_app = RequestUuidMiddleware(app.wsgi_app)


@app.route('/')
def hello_world():
    return 'Hello, World!'
