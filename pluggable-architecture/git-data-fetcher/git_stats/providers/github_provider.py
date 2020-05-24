from dateutil.parser import parse as parse_dt

import requests

from .base import BaseProvider, RepoStatistics

BASE_URL = "https://api.github.com"
# number PRs
# open_issues_count: 38,
# TODO create API token and sign in


class GitHubProvider(BaseProvider):
    @staticmethod
    def check(domain):
        return domain.lower() == "github.com"

    def repo_stats(self) -> RepoStatistics:
        # TODO error checking
        project_url = f"{BASE_URL}/repos/{str(self.repo)}"
        response = requests.get(project_url)
        data = response.json()

        return RepoStatistics(
            id=data["id"],
            description=data["description"],
            stars=data["stargazers_count"],
            forks=data["forks"],
            open_issues=data["open_issues"],
            last_activity=parse_dt(data["pushed_at"]),
        )
