import argparse
import os

import requests

GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN", None)


def generate_changelog(owner, repo, version):
    BASE_URL = f"https://api.github.com/repos/{owner}/{repo}"

    # get release date
    resp = requests.get(f"{BASE_URL}/releases/tags/{version}")
    if resp.status_code == 404:
        raise ValueError("Version does not exist")
    resp.raise_for_status()
    release_dt = resp.json()["published_at"]

    # get commit messages
    params = {"sha": "master", "since": release_dt}
    resp = requests.get(f"{BASE_URL}/commits", params=params)
    resp.raise_for_status()
    commit_messages = [item.get("commit", {}).get("message") for item in resp.json()]

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
