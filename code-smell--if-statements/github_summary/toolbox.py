from http import HTTPStatus
import os
import requests

GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN", None)


def get_github_events(github_username):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_OAUTH_TOKEN}",
        "Content-Type": "application/json",
    }
    url = f"https://api.github.com/users/{github_username}/events/public"

    resp = requests.get(url, headers=headers)

    if resp.status_code != HTTPStatus.OK:
        resp.raise_for_status()
    return resp.json()
