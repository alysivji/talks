import os
import argparse

from github import Github
from github.GithubException import UnknownObjectException

GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN", None)
BASE_URL = "https://api.github.com"


def generate_changelog(owner, repo, version):
    github = GitHubClient(GITHUB_OAUTH_TOKEN)
    release_dt = github.get_release_date(owner, repo, version)
    return github.get_commit_messages(owner, repo, release_dt)


class GitHubClient:
    def __init__(self, oauth_token):
        self._github = Github(oauth_token)

    def get_release_date(self, owner, repo, tag):
        repo = self._github.get_repo(f"{owner}/{repo}")
        try:
            tag = repo.get_release(tag)
        except UnknownObjectException:
            raise ValueError("Version does not exist")
        return tag.published_at

    def get_commit_messages(self, owner, repo, release_dt):
        repo = self._github.get_repo(f"{owner}/{repo}")
        commits = repo.get_commits(since=release_dt)
        commit_messages = [c.commit.message for c in commits]
        return commit_messages[::-1]


def parse_args():
    description = "Generate changelog for repository"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-r",
        "--repo",
        type=str,
        help="Full path to repository, (abc/xyz)",
        required=True,
    )
    parser.add_argument(
        "-v",
        "--version",
        type=str,
        help="Version to generate CHANGELOG from",
        required=True,
    )
    return vars(parser.parse_args())


if __name__ == "__main__":
    args = parse_args()
    try:
        owner, repo = args["repo"].split("/")
    except ValueError:
        raise ValueError("Invalid repo")
    version = args["version"]

    changelog = generate_changelog(owner, repo, version)
    print()
    print("\n".join(changelog))
