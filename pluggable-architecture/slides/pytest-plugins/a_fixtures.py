import pytest

from my_project.app import create_app


@pytest.fixture(scope="module")
def app():
    """Session-wide test `Flask` application.

    Establish an application context before running the tests.
    """
    app = create_app(testing=True)
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture(scope="module")
def client(app):
    """Create Flask test client where we can trigger test requests to app"""
    client = app.test_client()
    yield client


def test_ping_event(client, create_headers, subscription_payload):
    data = subscription_payload()
    headers = create_headers(data, event="ping", is_json_data=True)

    response = client.post("/github/event-subscription", headers=headers, json=data)

    assert response.status_code == 200
