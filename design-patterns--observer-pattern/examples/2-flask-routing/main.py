from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"page": "/"}

@app.route("/login")
def login():
    return {"page": "/login"}
