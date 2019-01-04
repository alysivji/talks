from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


@app.route("/")
def hello_world():
    users = User.query.all()

    user_output = []
    for user in users:
        user = {"id": user.id, "username": user.username, "email": user.email}
        user_output.append(user)

    return jsonify(user_output)


if __name__ == "__main__":
    db.create_all()  # initial database

    user1 = User(username="alan_turing", email="alan.turing@email.com")
    user2 = User(username="grace_hopper", email="grace.hopper@navy.gov")

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    app.run(port=5000)
