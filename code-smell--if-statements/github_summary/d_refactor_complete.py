from .toolbox import get_github_events


def perform(github_username):
    user_events = GitHubEGitHubUserEventsents(github_username)
    return user_events.generate_summary_text()


class GitHubEGitHubUserEventsents:
    def __init__(self, user):
        events = get_github_events(user)
        self.user = user
        self.event_types = self.classify_events(events)

    @staticmethod
    def classify_events(events):
        event_types = [Commits(), Stars(), PullRequestsOpened()]
        for event in events:
            for event_type in event_types:
                if event_type.matches_event(event):
                    event_type.append(event)
        return event_types

    def generate_summary_text(self):
        text = f"<@{self.user}> summary\n"
        for event_type in self.event_types:
            if len(event_type) > 0:
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
    def matches_event(event):
        return event["type"] == "PushEvent"

    def generate_summary_text(self):
        repos = list(set([event["repo"]["name"] for event in self.events]))
        commit_count = sum([len(event["payload"]["commits"]) for event in self.events])
        return (
            f">:arrow_up: {commit_count} commit(s) to "
            f"{len(repos)} repo(s): {', '.join(repos)}\n"
        )


class Stars(EventList):
    @staticmethod
    def matches_event(event):
        return event["type"] == "WatchEvent"

    def generate_summary_text(self):
        repos = list(set([event["repo"]["name"] for event in self.events]))
        return f">:star: {len(repos)} repo(s): {', '.join(repos)}\n"


class PullRequestsOpened(EventList):
    @staticmethod
    def matches_event(event):
        return (
            event["type"] == "PullRequestEvent"
            and event.get("payload", {}).get("action") == "opened"
        )

    def generate_summary_text(self):
        prs_made = [
            f'{event["repo"]["name"]}#{event["payload"]["pull_request"]["number"]}'
            for event in self.events
        ]
        return f">:arrow_heading_up: {len(prs_made)} PR(s): {', '.join(prs_made)}\n"
