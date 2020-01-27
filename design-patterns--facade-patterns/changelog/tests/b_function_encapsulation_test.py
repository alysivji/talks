import pytest
import responses

from changelog.b_function_encapsulation import (
    generate_changelog,
    get_release_date,
    get_commit_messages,
)


@responses.activate
@pytest.mark.unit
def test_get_release_date():
    responses.add(
        responses.GET,
        "http://url/releases/tags/1.0.0",
        json={"published_at": "2020-01-26"},
    )

    release_dt = get_release_date("http://url", "1.0.0")

    assert release_dt == "2020-01-26"


@responses.activate
@pytest.mark.unit
def test_get_commits():
    responses.add(
        responses.GET,
        "http://url/commits",
        json=[
            {"commit": {"message": "last commit"}},
            {"commit": {"message": "first commit"}},
        ],
    )
    messages = get_commit_messages("http://url", release_dt="value")

    assert messages == ["first commit", "last commit"]


@responses.activate
@pytest.mark.unit
def test_generate_changelog(mocker):

    mocker.patch("changelog.b_function_encapsulation.get_release_date")
    commit_mock = mocker.patch("changelog.b_function_encapsulation.get_commit_messages")
    commit_mock.return_value = ["first commit", "last commit"]

    messages = generate_changelog("owner", "repo", "1.0.0")

    assert messages == ["first commit", "last commit"]
