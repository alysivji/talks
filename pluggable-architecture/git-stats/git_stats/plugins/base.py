from git_stats.download import RepoStatistics


class BasePlugin:
    def __init__(self, repo):
        self.repo = repo

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    @staticmethod
    def check(domain) -> bool:
        raise NotImplementedError

    def repo_stats(self) -> RepoStatistics:
        raise NotImplementedError
