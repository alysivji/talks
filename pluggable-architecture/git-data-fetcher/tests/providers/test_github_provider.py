import pytest

from git_stats.download import RepoDetails
from git_stats.providers.github_provider import GitHubProvider


@pytest.mark.vcr()
def test_github_provider():
    repo = RepoDetails(organization="busy-beaver-dev", repo="busy-beaver")
    client = GitHubProvider(repo)

    result = client.repo_stats()

    assert result.id == 158856915
    assert result.description == "The Chicago Python Community Engagement Slack bot"
    assert result.stars == 54
    assert result.forks == 23
    assert result.open_issues == 35
