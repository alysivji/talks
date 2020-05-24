from git_data_fetcher.download import GitFetcher


def test_url_parser():
    url = "https://gitlab.com/pycqa/flake8"

    client = GitFetcher(url)

    details = client.repo
    assert details.domain == "gitlab.com"
    assert details.organization == "pycqa"
    assert details.repo == "flake8"
