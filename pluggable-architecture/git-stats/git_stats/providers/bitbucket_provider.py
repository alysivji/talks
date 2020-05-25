from dateutil.parser import parse as parse_dt

import requests

from .base import BaseProvider, RepoStatistics

BASE_URL = "https://api.bitbucket.org/2.0"


class BitBucketProvider(BaseProvider):
    """BitBucket Provider

    API Docs: https://confluence.atlassian.com/bitbucket/rest-apis-222724129.html
    """
    @staticmethod
    def check(domain):
        return domain.lower() == "bitbucket.org"

    def repo_stats(self) -> RepoStatistics:
        project_url = f"{BASE_URL}/repositories/{str(self.repo)}"
        response = requests.get(project_url)
        data = response.json()

        return RepoStatistics(
            id=data["uuid"],
            description=data["description"],
            stars=None,
            forks=None,
            open_issues=None,
            last_activity=parse_dt(data["updated_on"]),
        )
