import pytest

from git_stats.download import RepoDetails
from git_stats.plugins.gitlab_plugin import GitLabPlugin


@pytest.mark.vcr()
def test_gitlab_plugin():
    repo = RepoDetails(organization="pycqa", repo="flake8")
    client = GitLabPlugin(repo)

    result = client.repo_stats()

    assert result.id == 88891
    assert "flake8 is a python tool that glues together pep8" in result.description
    assert result.stars == 364
    assert result.forks == 178
