#!/usr/bin/env python3

import argparse
import pprint

import requests

ACTIVITY_URL = "https://api.github.com/users/{username}/events/public"
headers = {
    "content-type": "application/json",
    "User-agent": "SivScript -- MostRecentActvity",
}


def fetch_last_event(username: str) -> dict:
    resp = requests.get(ACTIVITY_URL.format(username=username), headers=headers)
    pprint.pprint(resp.json()[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recent GitHub Activity")
    parser.add_argument("--github", type=str, required=True, help="GitHub username")
    args = parser.parse_args()
    username = args.github

    fetch_last_event(username)
