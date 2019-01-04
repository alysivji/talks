import pytest

from app.main import app


@pytest.mark.skip
def test_to_game_coverage():
    # Arrange
    client = app.test_client()

    # Act
    body = {"url": "https://www.meetup.com/indypy/"}
    response = client.post("/top-word", json=body)

    return response
