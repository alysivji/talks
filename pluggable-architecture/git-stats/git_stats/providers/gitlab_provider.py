from dateutil.parser import parse as parse_dt
from urllib.parse import quote_plus

import requests

from .base import BaseProvider, RepoStatistics

BASE_URL = "https://gitlab.com/api/v4"


class GitLabProvider(BaseProvider):
    """GitLab Provider

    API Docs: https://docs.gitlab.com/ee/api/README.html
    """

    @staticmethod
    def check(domain):
        return domain.lower() == "gitlab.com"

    def repo_stats(self) -> RepoStatistics:
        encoded_repo = quote_plus(str(self.repo))
        project_url = f"{BASE_URL}/projects/{encoded_repo}"
        response = requests.get(project_url)
        data = response.json()

        return RepoStatistics(
            id=data["id"],
            description=data["description"],
            stars=data["star_count"],
            forks=data["forks_count"],
            open_issues=None,  # =data["open_issues_count"],
            last_activity=parse_dt(data["last_activity_at"]),
        )
