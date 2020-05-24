from typing import NamedTuple


class RepoStatistics(NamedTuple):
    id: int
    stars: int
    forks: int
    open_issues: int = None


class BaseProvider:
    def __init__(self, repo):
        self.repo = repo

    def get_commits(self):
        pass
