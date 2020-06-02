from datetime import datetime
from typing import NamedTuple


class RepoStatistics(NamedTuple):
    id: int
    description: str
    stars: int
    forks: int
    open_issues: int
    last_activity: datetime


class BasePlugin:
    def __init__(self, repo):
        self.repo = repo

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


    # TODO add check

    def repo_stats(self) -> RepoStatistics:
        pass
