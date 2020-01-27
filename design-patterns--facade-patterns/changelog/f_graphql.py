import os
import argparse

from sgqlc.endpoint.requests import RequestsEndpoint

GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN", None)
BASE_URL = "https://api.github.com"


def generate_changelog(owner, repo, version):
    github = GitHubClient(GITHUB_OAUTH_TOKEN)
    release_dt = github.get_release_date(owner, repo, version)
    return github.get_commit_messages(owner, repo, release_dt)


class GitHubClient:
    def __init__(self, oauth_token):
        headers = {"Authorization": f"Bearer {GITHUB_OAUTH_TOKEN}"}
        self.endpoint = RequestsEndpoint("https://api.github.com/graphql", headers)

    def get_release_date(self, owner, repo, tag):
        query = """
        query findReleaseDt($owner: String!, $repo: String!, $tag: String!) {
            repository(owner: $owner, name: $repo) {
                release(tagName: $tag) {
                    publishedAt
                }
            }
        }
        """
        variables = {"owner": owner, "repo": repo, "tag": tag}
        data = self.endpoint(query, variables)
        try:
            return data["data"]["repository"]["release"]["publishedAt"]
        except TypeError:  # returns {"release": None} if tag does not exist
            raise ValueError("Version does not exist")

    def get_commit_messages(self, owner, repo, release_dt):
        query = """
        query commitsSinceDt($owner: String!, $repo: String!, $branch: String!, $since_dt: GitTimestamp) {
            repository(owner: $owner, name: $repo) {
                object(expression: $branch) {
                    ... on Commit {
                        history(since: $since_dt) {
                            nodes {
                                messageHeadline
                            }
                        }
                    }
                }
            }
        }
        """  # noqa
        variables = {
            "owner": owner,
            "repo": repo,
            "branch": "master",
            "since_dt": release_dt,
        }
        data = self.endpoint(query, variables)
        if "errors" in data:
            # loop thru this: data["errors"][0]["message"]
            raise ValueError()

        commits = data["data"]["repository"]["object"]["history"]["nodes"]
        commit_messages = [commit["messageHeadline"] for commit in commits]
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
