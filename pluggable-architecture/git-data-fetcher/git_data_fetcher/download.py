from typing import List, NamedTuple
from urllib.parse import urlparse


class RepoDetails(NamedTuple):
    organization: str
    repo: str


class GitFetcher:
    providers = []

    def __init__(self, url, external: List = None):
        domain, self.repo = self._parse_url(url)

    def _parse_url(self, url):
        url_parts = urlparse(url)
        parts = url_parts.path.split("/")
        return url_parts.netloc, RepoDetails(organization=parts[1], repo=parts[2])

    def get_commits(self):
        pass
