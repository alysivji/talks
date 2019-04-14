from datetime import datetime
import gettext

from .event_list import (
    CommitsList,
    CreatedReposList,
    ForkedReposList,
    IssuesOpenedList,
    PublicizedReposList,
    PullRequestsList,
    ReleasesPublishedList,
    StarredReposList,
)
from busy_beaver import github
from busy_beaver.models import User


def generate_summary_text(user, boundary_dt):
    """This method is in a different module"""
    user_events = GitHubUserEvents(user, boundary_dt)
    return user_events.generate_summary_text()


class GitHubUserEvents:
    def __init__(self, user: User, boundary_dt: datetime):
        self.user = user
        self.events = {  # this is the order of summary output
            "releases_published": ReleasesPublishedList(),
            "created_repos": CreatedReposList(),
            "publicized_repos": PublicizedReposList(),
            "forked_repos": ForkedReposList(),
            "pull_requests": PullRequestsList(),
            "issues_opened": IssuesOpenedList(),
            "commits": CommitsList(),
            "starred_repos": StarredReposList(),
        }

        timeline = github.user_activity_after(user.github_username, boundary_dt)
        self._classify_events(timeline)

    def generate_summary_text(self):
        summary = ""
        for event_type, events in self.events.items():
            summary += events.generate_summary_text()

        if not summary:
            return ""

        user_info = "<@{slack_id}> as <https://github.com/{github_id}|{github_id}>\n"
        params = {
            "slack_id": self.user.slack_id,
            "github_id": self.user.github_username,
        }
        return user_info.format(**params) + summary + "\n"

    def _classify_events(self, timeline):
        for event in timeline:
            data = event["payload"]
            if event["type"] == "CreateEvent" and data.get("ref_type") == "repository":
                self.events["created_repos"].append(event)
            elif event["type"] == "ForkEvent":
                self.events["forked_repos"].append(event)
            elif event["type"] == "IssuesEvent" and data.get("action") == "opened":
                self.events["issues_opened"].append(event)
            elif event["type"] == "PublicEvent":
                self.events["publicized_repos"].append(event)
            elif event["type"] == "PullRequestEvent" and data.get("action") == "opened":
                self.events["pull_requests"].append(event)
            elif event["type"] == "PushEvent":
                self.events["commits"].append(event)
            elif event["type"] == "ReleaseEvent":
                self.events["releases_published"].append(event)
            elif event["type"] == "WatchEvent" and data.get("action") == "started":
                self.events["starred_repos"].append(event)


# Singular or Plural Form in Summary
commit_form = lambda n: gettext.ngettext("commit", "commits", n)  # noqa
issue_form = lambda n: gettext.ngettext("issue", "issues", n)  # noqa
pr_form = lambda n: gettext.ngettext("PR", "PRs", n)  # noqa
release_form = lambda n: gettext.ngettext("release", "releases", n)  # noqa
repo_form = lambda n: gettext.ngettext("repo", "repos", n)  # noqa


class EventList:
    def __init__(self):
        self.events = []

    def __repr__(self):
        return repr(self.events)

    def append(self, item):
        self.events.append(item)

    def generate_summary_text(self):
        if not self.events:
            return ""
        event_links = set([self._generate_link(event) for event in self.events])
        return self._format_text(event_links)

    def _format_text(self, links):
        return NotImplemented

    @staticmethod
    def _generate_link(event):
        repo_url = event["repo"]["url"]
        repo_url = repo_url.replace("api.github.com/repos/", "www.github.com/")
        repo_name = event["repo"]["name"]
        return f"<{repo_url}|{repo_name}>"


class CommitsList(EventList):
    def _format_text(self, links):
        num = len(links)
        n_commits = sum([event["payload"]["distinct_size"] for event in self.events])
        return (
            f">:arrow_up: {n_commits} {commit_form(n_commits)} to "
            f"{num} {repo_form(num)}: {', '.join(links)}\n"
        )


class CreatedReposList(EventList):
    def _format_text(self, links):
        num = len(links)
        return f">:sparkles: {num} new {repo_form(num)}: {', '.join(links)}\n"


class ForkedReposList(EventList):
    def _format_text(self, links):
        emoji = ":fork_and_knife:"
        num = len(links)
        return f">{emoji} {num} forked {repo_form(num)}: {', '.join(links)}\n"


class IssuesOpenedList(EventList):
    def _format_text(self, links):
        num = len(links)
        return f">:interrobang: {num} new {issue_form(num)}: {', '.join(links)}\n"

    @staticmethod
    def _generate_link(event):
        issue_url = event["payload"]["issue"]["html_url"]
        issue_number = event["payload"]["issue"]["number"]
        repo_name = event["repo"]["name"]
        return f"<{issue_url}|{repo_name}#{issue_number}>"


class PublicizedReposList(EventList):
    def _format_text(self, links):
        emoji = ":speaking_head_in_silhouette:"
        num = len(links)
        return f">{emoji} {num} {repo_form(num)} open-sourced: {', '.join(links)}\n"


class PullRequestsList(EventList):
    def _format_text(self, links):
        num = len(links)
        return f">:arrow_heading_up: {num} {pr_form(num)}: {', '.join(links)}\n"

    @staticmethod
    def _generate_link(event):
        pr_url = event["payload"]["pull_request"]["html_url"]
        pr_number = event["payload"]["pull_request"]["number"]
        repo_name = event["repo"]["name"]
        return f"<{pr_url}|{repo_name}#{pr_number}>"


class ReleasesPublishedList(EventList):
    def _format_text(self, links):
        num = len(links)
        return f">:ship: {num} new {release_form(num)}: {', '.join(links)}\n"


class StarredReposList(EventList):
    def _format_text(self, links):
        num = len(links)
        return f">:star: {num} {repo_form(num)}: {', '.join(links)}\n"
