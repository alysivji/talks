from dateutil.parser import parse as parse_dt
from urllib.parse import quote_plus

import requests

from .base import BaseProvider, RepoStatistics

# https://gitlab.com/api/v4/projects/pycqa%2Fflake8
BASE_URL = "https://gitlab.com/api/v4"
# number PRs
# open_issues_count: 38,
# TODO create API token and sign in
# TODO last_updated_at


class GitLabProvider(BaseProvider):
    def repo_stats(self) -> RepoStatistics:
        # TODO error checking
        encoded_repo = quote_plus(str(self.repo))
        project_url = f"{BASE_URL}/projects/{encoded_repo}"
        response = requests.get(project_url)
        data = response.json()

        return RepoStatistics(
            id=data["id"],
            stars=data["star_count"],
            forks=data["forks_count"],
            open_issues=None,  # =data["open_issues_count"],
            last_activity=parse_dt(data["last_activity_at"]),
        )
