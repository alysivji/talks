"""Data Transfer Objects"""

from datetime import datetime
from typing import NamedTuple


class RepoDetails(NamedTuple):
    organization: str
    repo: str

    def __str__(self):
        return self.organization + "/" + self.repo


class RepoStatistics(NamedTuple):
    id: int
    description: str
    stars: int
    forks: int
    open_issues: int
    last_activity: datetime
