from collections import defaultdict
from .toolbox import get_github_events


def perform(github_username):
    user_events = get_github_events(github_username)
    classified_events = extract_events_of_interest(user_events)
    return generate_summary_from_events(github_username, classified_events)


def extract_events_of_interest(events):
    classified_events = defaultdict(list)
    for event in events:
        if event["type"] == "PushEvent":
            classified_events["PushEvent"].append(event)
        elif event["type"] == "WatchEvent":
            classified_events["WatchEvent"].append(event)
        elif (
            event["type"] == "PullRequestEvent"
            and event.get("payload", {}).get("action") == "opened"
        ):
            classified_events["PullRequestEvent"].append(event)
    return classified_events


def generate_summary_from_events(github_username, classified_events):
    text = f"<@{github_username}> summary\n"
    for event_type, events in classified_events.items():
        repos = list(set([event["repo"]["name"] for event in events]))
        repo_count = len(repos)

        if event_type == "PushEvent":
            commit_count = sum([len(event["payload"]["commits"]) for event in events])
            text += (
                f">:arrow_up: {commit_count} commit(s) to "
                f"{repo_count} repo(s): {', '.join(repos)}\n"
            )
        elif event_type == "WatchEvent":
            text += f">:star: {repo_count} repo(s): {', '.join(repos)}\n"
        elif event_type == "PullRequestEvent":
            prs_made = [
                f'{event["repo"]["name"]}#{event["payload"]["pull_request"]["number"]}'
                for event in events
            ]
            text += f">:arrow_heading_up: {repo_count} PR(s): {', '.join(prs_made)}\n"
    return text
