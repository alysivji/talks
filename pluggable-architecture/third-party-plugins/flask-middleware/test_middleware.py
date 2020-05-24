from flask import Flask, request
import pytest

from middleware import RequestUuidMiddleware


@pytest.fixture(scope="session")
def app():
    app = Flask(__name__)
    app.wsgi_app = RequestUuidMiddleware(app.wsgi_app)

    @app.route('/')
    def hello_world():
        return request.environ.get("request_id")

    ctx = app.app_context()
    ctx.push()
    yield app

    ctx.pop()


@pytest.fixture(scope="session")
def client(app):
    client = app.test_client()
    yield client


def test_middleware(client):
    result = client.get("/")
    assert len(result.data) > 0


def test_middleware_with_request_id(client):
    result = client.get("/", headers={"X-Request-ID": "abc"})
    assert result.data == b"abc"
