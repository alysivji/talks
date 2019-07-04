from .toolbox import get_github_events


def perform(github_username):
    events = get_github_events(github_username)
    event_types = [Commits(), Stars(), PullRequests()]

    for event in events:
        for event_type in event_types:
            if event_type.check(event):
                event_type.append(event)

    text = f"<@{github_username}> summary\n"
    for event_type in event_types:
        if len(event_type):
            text += event_type.generate_summary_text()

    return text


class EventList:
    def __init__(self):
        self.events = []

    def __len__(self):
        return len(self.events)

    def append(self, item):
        self.events.append(item)


class Commits(EventList):
    @staticmethod
    def check(event):
        return True if event["type"] == "PushEvent" else False

    def generate_summary_text(self):
        repos = list(set([event["repo"]["name"] for event in self.events]))
        commit_count = sum([len(event["payload"]["commits"]) for event in self.events])
        return (
            f">:arrow_up: {commit_count} commit(s) to "
            f"{len(repos)} repo(s): {', '.join(repos)}\n"
        )


class Stars(EventList):
    @staticmethod
    def check(event):
        return True if event["type"] == "WatchEvent" else False

    def generate_summary_text(self):
        repos = list(set([event["repo"]["name"] for event in self.events]))
        return f">:star: {len(repos)} repo(s): {', '.join(repos)}\n"


class PullRequests(EventList):
    @staticmethod
    def check(event):
        return (
            True
            if event["type"] == "PullRequestEvent"
            and event.get("payload", {}).get("action") == "opened"
            else False
        )

    def generate_summary_text(self):
        prs_made = [
            f'{event["repo"]["name"]}#{event["payload"]["pull_request"]["number"]}'
            for event in self.events
        ]
        return f">:arrow_heading_up: {len(prs_made)} PR(s): {', '.join(prs_made)}\n"
