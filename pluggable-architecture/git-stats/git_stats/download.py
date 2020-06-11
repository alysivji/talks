from urllib.parse import urlparse

from .dto import RepoDetails, RepoStatistics
from .plugins.bitbucket_plugin import BitBucketPlugin
from .plugins.github_plugin import GitHubPlugin
from .plugins.gitlab_plugin import GitLabPlugin

plugins = [BitBucketPlugin, GitHubPlugin, GitLabPlugin]


class GitApiClient:
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

    def get_stats(self) -> RepoStatistics:
        return self.plugin.repo_stats()
