from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    users = ["Alan Turing", "Grace Hopper"]
    return render_template("user.html", users=users)


if __name__ == "__main__":
    app.run()
