from typing import NamedTuple
from urllib.parse import urlparse

from .providers.github_provider import GitHubProvider
from .providers.gitlab_provider import GitLabProvider

providers = [GitHubProvider, GitLabProvider]


class RepoDetails(NamedTuple):
    organization: str
    repo: str

    def __str__(self):
        return self.organization + "/" + self.repo


class GitFetcher:
    def __init__(self, url):
        domain, self.repo = self._parse_url(url)
        for provider in providers:
            if provider.check(domain):
                self.provider = provider(self.repo)
                return
        else:
            raise ValueError(f"{domain} not supported")

    def _parse_url(self, url):
        url_parts = urlparse(url)
        parts = url_parts.path.split("/")
        return url_parts.netloc, RepoDetails(organization=parts[1], repo=parts[2])

    def get_stats(self):
        return self.provider.repo_stats()
