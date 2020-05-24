# https://gitlab.com/api/v4/projects/pycqa%2Fflake8
# - get PRs
from urllib.parse import quote_plus
import requests
from .base import BaseProvider

# https://gitlab.com/api/v4/projects/pycqa%2Fflake8
BASE_URL = "https://gitlab.com/api/v4/"
# number PRs
# number open issues
# number of stars
# number of forks
# star_count: 364,
# forks_count: 178,
# open_issues_count: 38,


class GitLabProvider(BaseProvider):
    def __init__(self, repo):
        super().__init__(repo)
        self.repo_id = self._get_repo_id(repo)

    @staticmethod
    def _get_repo_id(repo):
        # TODO error checking
        encoded_repo = quote_plus(str(repo))
        project_url = f"{BASE_URL}/projects/{encoded_repo}"
        response = requests.get(project_url)
        return response.json()["id"]
