import pytest

from git_data_fetcher.download import RepoDetails
from git_data_fetcher.providers.gitlab_provider import GitLabProvider


@pytest.mark.vcr()
def test_gitlab_provider():
    repo = RepoDetails(organization="pycqa", repo="flake8")
    client = GitLabProvider(repo)

    result = client.repo_stats()

    assert result.id == 88891
    assert "flake8 is a python tool that glues together pep8" in result.description
    assert result.stars == 364
    assert result.forks == 178
