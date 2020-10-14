import os
from unittest.mock import MagicMock
import pytest

from changelog.e_vcr import generate_changelog, GitHubClient


class GitHubClientStub:
    def __init__(self, commit_messages=None):
        self.commit_messages = commit_messages
        self.mock = MagicMock()

    def get_release_date(self, *args, **kwargs):
        self.mock(*args, **kwargs)

    def get_commit_messages(self, *args, **kwargs):
        self.mock(*args, **kwargs)
        return self.commit_messages


@pytest.mark.unit
def test_generate_changelog(mocker):
    github_mock = mocker.patch("changelog.e_vcr.GitHubClient")
    commit_messages = ["first commit", "last commit"]
    github_mock.return_value = GitHubClientStub(commit_messages)

    messages = generate_changelog("owner", "repo", "1.0.0")

    assert messages == ["first commit", "last commit"]


@pytest.mark.vcr(cassette_library_dir="changelog/tests/cassettes/rest")
@pytest.mark.integration
def test_github_client_get_release_date():
    GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN", None)
    github = GitHubClient(GITHUB_OAUTH_TOKEN)

    release_dt = github.get_release_date("busy-beaver-dev", "busy-beaver", "1.3.2")

    assert release_dt == "2020-01-26T19:04:10Z"


@pytest.mark.vcr(cassette_library_dir="changelog/tests/cassettes/rest")
@pytest.mark.integration
def test_github_client_get_commit_messages():
    GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN", None)
    github = GitHubClient(GITHUB_OAUTH_TOKEN)

    release_dt = "2020-01-25T19:04:10Z"
    messages = github.get_commit_messages("busy-beaver-dev", "busy-beaver", release_dt)

    assert "Automate import sorting with isort (#227)" in messages
