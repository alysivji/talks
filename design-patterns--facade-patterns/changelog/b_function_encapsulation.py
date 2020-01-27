import argparse
import requests


def generate_changelog(owner, repo, version):
    BASE_URL = f"https://api.github.com/repos/{owner}/{repo}"
    release_dt = get_release_date(BASE_URL, version)
    return get_commit_messages(BASE_URL, release_dt)


def get_release_date(base_url, version):
    resp = requests.get(f"{base_url}/releases/tags/{version}")
    if resp.status_code == 404:
        raise ValueError("Version does not exist")
    resp.raise_for_status()
    return resp.json()["published_at"]


def get_commit_messages(base_url, release_dt):
    params = {"sha": "master", "since": release_dt}
    resp = requests.get(f"{base_url}/commits", params=params)
    resp.raise_for_status()
    messages = [item.get("commit", {}).get("message") for item in resp.json()]
    return messages[::-1]


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
