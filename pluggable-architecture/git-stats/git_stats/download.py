from typing import NamedTuple
from urllib.parse import urlparse

from .plugins.bitbucket_plugin import BitBucketPlugin
from .plugins.github_plugin import GitHubPlugin
from .plugins.gitlab_plugin import GitLabPlugin

plugins = [BitBucketPlugin, GitHubPlugin, GitLabPlugin]


class RepoDetails(NamedTuple):
    organization: str
    repo: str

    def __str__(self):
        return self.organization + "/" + self.repo


class GitFetcher:
    def __init__(self, url):
        domain, self.repo = self._parse_url(url)
        for plugin in plugins:
            if plugin.check(domain):
                self.plugin = plugin(self.repo)
                return
        else:
            raise ValueError(f"{domain} not supported")

    def _parse_url(self, url):
        url_parts = urlparse(url)
        parts = url_parts.path.split("/")
        return url_parts.netloc, RepoDetails(organization=parts[1], repo=parts[2])

    def get_stats(self):
        return self.plugin.repo_stats()
