from typing import List, NamedTuple
from urllib.parse import urlparse


class RepoDetails(NamedTuple):
    domain: str
    organization: str
    repo: str


class GitFetcher:
    def __init__(self, url, external: List = None):
        self.repo = self._parse_url(url)
        if not external:
            external = []
        self.external = external

    def get_commits(self):
        pass

    def _parse_url(self, url):
        url_parts = urlparse(url)
        parts = url_parts.path.split("/")
        return RepoDetails(
            domain=url_parts.netloc, organization=parts[1], repo=parts[2]
        )
