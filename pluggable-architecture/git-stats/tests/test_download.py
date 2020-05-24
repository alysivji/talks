from git_stats.download import GitFetcher


def test_url_parser():
    url = "https://gitlab.com/pycqa/flake8"

    client = GitFetcher(url)

    repo_details = client.repo
    assert repo_details.organization == "pycqa"
    assert repo_details.repo == "flake8"
