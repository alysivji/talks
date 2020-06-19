from urllib.parse import quote_plus

import requests

from .base import BasePlugin
from git_stats.dto import RepoStatistics


class GitLabPlugin(BasePlugin):
    @staticmethod
    def check(domain):
        return domain.lower() == "gitlab.com"

    def repo_stats(self) -> RepoStatistics:
        encoded_repo = quote_plus(self.repo)
        project_url = f"https://gitlab.com/api/v4/projects/{encoded_repo}"
        response = requests.get(project_url)
        data = response.json()

        return RepoStatistics(
            id=data["id"],
            description=data["description"],
            stars=data["star_count"],
            forks=data["forks_count"],
            open_issues=None,
            last_activity=data["last_activity_at"],
        )
