import pytest

from git_data_fetcher.download import RepoDetails
from git_data_fetcher.providers.gitlab_provider import GitLabProvider


@pytest.mark.vcr()
def test_gitlab_provider():
    repo = RepoDetails(organization="pycqa", repo="flake8")
    client = GitLabProvider(repo)
    assert client.repo_id == 88891
