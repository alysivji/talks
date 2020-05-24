from datetime import datetime
from typing import NamedTuple


class RepoStatistics(NamedTuple):
    id: int
    stars: int
    forks: int
    open_issues: int
    last_activity: datetime


class BaseProvider:
    def __init__(self, repo):
        self.repo = repo

    def get_commits(self) -> RepoStatistics:
        pass
