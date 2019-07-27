import inflect
from .toolbox import get_github_events

inflector = inflect.engine()


def perform(github_username):
    user_events = GitHubUserEvents(github_username)
    return user_events.generate_summary_text()


class GitHubUserEvents:
    def __init__(self, user):
        events = get_github_events(user)
        self.user = user
        self.event_types = self.classify_events(events)

    @staticmethod
    def classify_events(events):
        event_types = [  # this is the order of summary output
            ReleasesPublished(),
            ReposCreated(),
            ReposPublicized(),
            ReposForked(),
            PullRequestsOpened(),
            IssuesOpened(),
            Commits(),
            Stars(),
        ]
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

    def generate_summary_text(self):
        if not self.events:
            return ""
        event_links = set([self._generate_link(event) for event in self.events])
        return self._format_text(event_links)

    @staticmethod
    def _generate_link(event):
        repo_url = event["repo"]["url"]
        repo_url = repo_url.replace("api.github.com/repos/", "www.github.com/")
        repo_name = event["repo"]["name"]
        return f"<{repo_url}|{repo_name}>"

    def _format_text(self, links):
        num = len(links)
        noun = inflector.plural(self.NOUN, num)
        link_output = ", ".join(links)
        return f">{self.EMOJI} {num} {noun} {link_output}\n"


class Commits(EventList):
    EMOJI = ":arrow_up:"
    NOUN = "repo"

    @staticmethod
    def matches_event(event):
        return event["type"] == "PushEvent"

    def _format_text(self, links):
        num_repos = len(links)
        repo_noun = inflector.plural(self.NOUN, num_repos)

        num_commits = sum([event["payload"]["distinct_size"] for event in self.events])
        commit_noun = inflector.plural("commit", num_commits)
        return (
            f">{self.EMOJI} {num_commits} {commit_noun} "
            f"{num_repos} {repo_noun}: {', '.join(links)}\n"
        )


class IssuesOpened(EventList):
    EMOJI = ":interrobang:"
    NOUN = "new issue"

    @staticmethod
    def matches_event(event):
        return (
            event["type"] == "IssuesEvent"
            and event.get("payload", {}).get("action") == "opened"
        )

    @staticmethod
    def _generate_link(event):
        issue_url = event["payload"]["issue"]["html_url"]
        issue_number = event["payload"]["issue"]["number"]
        repo_name = event["repo"]["name"]
        return f"<{issue_url}|{repo_name}#{issue_number}>"


class PullRequestsOpened(EventList):
    EMOJI = ":arrow_heading_up:"
    NOUN = "PR"

    @staticmethod
    def matches_event(event):
        return (
            event["type"] == "PullRequestEvent"
            and event.get("payload", {}).get("action") == "opened"
        )

    @staticmethod
    def _generate_link(event):
        pr_url = event["payload"]["pull_request"]["html_url"]
        pr_number = event["payload"]["pull_request"]["number"]
        repo_name = event["repo"]["name"]
        return f"<{pr_url}|{repo_name}#{pr_number}>"


class ReleasesPublished(EventList):
    EMOJI = ":ship:"
    NOUN = "new release"

    @staticmethod
    def matches_event(event):
        return event["type"] == "ReleaseEvent"


class ReposCreated(EventList):
    EMOJI = ":sparkles:"
    NOUN = "new repo"

    @staticmethod
    def matches_event(event):
        return (
            event["type"] == "CreateEvent"
            and event.get("payload", {}).get("ref_type") == "repository"
        )


class ReposForked(EventList):
    EMOJI = ":fork_and_knife:"
    NOUN = "forked repo"

    @staticmethod
    def matches_event(event):
        return event["type"] == "ForkEvent"


class ReposPublicized(EventList):
    EMOJI = ":speaking_head_in_silhouette:"
    NOUN = "open-sourced repo"

    @staticmethod
    def matches_event(event):
        return event["type"] == "PublicEvent"


class Stars(EventList):
    EMOJI = ":star:"
    NOUN = "repo"

    @staticmethod
    def matches_event(event):
        return event["type"] == "WatchEvent"
