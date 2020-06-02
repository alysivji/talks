import pytest

from git_stats.download import RepoDetails
from git_stats.plugins.bitbucket_plugin import BitBucketPlugin


@pytest.mark.vcr()
def test_bitbucket_plugin():
    repo = RepoDetails(organization="tutorials", repo="tutorials.bitbucket.org")
    client = BitBucketPlugin(repo)

    result = client.repo_stats()

    assert '9970a9b6-2d86-413f-8555-da8e1ac0e542' in result.id
    assert result.description == "Site for tutorial101 files"
