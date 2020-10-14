import pytest
import responses

from changelog.a_use_requests import generate_changelog


@responses.activate
@pytest.mark.unit
def test_generate_changelog():
    # Arrange
    responses.add(
        responses.GET,
        "https://api.github.com/repos/owner/repo/releases/tags/1.0.0",
        json={"published_at": "2020-01-26"},
    )

    responses.add(
        responses.GET,
        "https://api.github.com/repos/owner/repo/commits",
        json=[
            {"commit": {"message": "last commit"}},
            {"commit": {"message": "first commit"}},
        ],
    )

    # Act
    changelog = generate_changelog("owner", "repo", "1.0.0")

    # Assert
    assert changelog == ["first commit", "last commit"]
