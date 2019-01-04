from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)


@app.route("/")
def hello():
    # can replace most of this logic with marshmallow
    users = User.query.filter_by(name="Grace Hopper").all()

    user_output = [
        {"name": user.name, "email": user.email}
        for user in users
    ]
    return jsonify(user_output)


if __name__ == "__main__":
    db.create_all()

    alan = User(name="Alan Turing", email="alan.turing@me.com")
    grace = User(name="Grace Hopper", email="grace.hopper@me.com")
    tim = User(name="Tim Berners-Lee", email="tim@internet.com")

    db.session.add(alan)
    db.session.add(grace)
    db.session.add(tim)
    db.session.commit()

    app.run()
