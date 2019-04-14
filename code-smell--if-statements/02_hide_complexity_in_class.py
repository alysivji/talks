from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import gettext

from ..adapters.github import GitHubAdapter
from ..config import oauth_token
from ..models import User

github = GitHubAdapter(oauth_token)


def generate_summary(user: User, boundary_dt: datetime):
    user_timeline = github.user_activity_after(user.github_username, boundary_dt)
    user_events = _classify_events(user, user_timeline)
    return user_events.generate_summary_text()


def _classify_events(user: User, timeline: List[dict]):
    user_events = GitHubUserEvents(user=user)
    for event in timeline:
        payload = event["payload"]
        if event["type"] == "CreateEvent" and payload.get("ref_type") == "repository":
            user_events.created_repos.append(event)
        elif event["type"] == "ForkEvent":
            user_events.forked_repos.append(event)
        elif event["type"] == "IssuesEvent" and payload.get("action") == "opened":
            user_events.issues_opened.append(event)
        elif event["type"] == "PublicEvent":
            user_events.publicized_repos.append(event)
        elif event["type"] == "PullRequestEvent" and payload.get("action") == "opened":
            user_events.pull_requests.append(event)
        elif event["type"] == "PushEvent":
            user_events.commits.append(event)
        elif event["type"] == "ReleaseEvent":
            user_events.releases_published.append(event)
        elif event["type"] == "WatchEvent" and payload.get("action") == "started":
            user_events.starred_repos.append(event)
    return user_events


@dataclass
class GitHubUserEvents:
    user: User
    created_repos: List[dict] = field(default_factory=list)
    forked_repos: List[dict] = field(default_factory=list)
    issues_opened: List[dict] = field(default_factory=list)
    publicized_repos: List[dict] = field(default_factory=list)
    pull_requests: List[dict] = field(default_factory=list)
    commits: List[dict] = field(default_factory=list)
    releases_published: List[dict] = field(default_factory=list)
    starred_repos: List[dict] = field(default_factory=list)

    def generate_summary_text(self):
        summary = ""
        summary += self._releases_published_text()
        summary += self._create_repos_text()
        summary += self._publicized_repos_text()
        summary += self._forked_repos_text()
        summary += self._pull_requests_text()
        summary += self._issues_opened_text()
        summary += self._commits_text()
        summary += self._starred_repos_text()

        if not summary:
            return ""

        user_info = "<@{slack_id}> as <https://github.com/{github_id}|{github_id}>\n"
        params = {
            "slack_id": self.user.slack_id,
            "github_id": self.user.github_username,
        }
        return user_info.format(**params) + summary + "\n"

    def _releases_published_text(self):
        if not self.releases_published:
            return ""

        r = [generate_repo_link(event) for event in self.releases_published]
        return f">:ship: {len(r)} new {release_form(len(r))}: {', '.join(r)}\n"

    def _create_repos_text(self):
        if not self.created_repos:
            return ""

        r = [generate_repo_link(event) for event in self.created_repos]
        return f">:sparkles: {len(r)} new {repo_form(len(r))}: {', '.join(r)}\n"

    def _publicized_repos_text(self):
        if not self.publicized_repos:
            return ""

        emoji = ":speaking_head_in_silhouette:"
        r = [generate_repo_link(event) for event in self.publicized_repos]
        return f">{emoji} {len(r)} {repo_form(len(r))} open-sourced: {', '.join(r)}\n"

    def _forked_repos_text(self):
        if not self.forked_repos:
            return ""

        emoji = ":fork_and_knife:"
        r = [generate_repo_link(event) for event in self.forked_repos]
        return f">{emoji} {len(r)} forked {repo_form(len(r))}: {', '.join(r)}\n"

    def _pull_requests_text(self):
        if not self.pull_requests:
            return ""

        r = [generate_repo_link(event) for event in self.pull_requests]
        return f">:arrow_heading_up: {len(r)} {pr_form(len(r))}: {', '.join(r)}\n"

    def _issues_opened_text(self):
        if not self.issues_opened:
            return ""

        r = [generate_issue_link(event) for event in self.issues_opened]
        return f">:interrobang: {len(r)} new {issue_form(len(r))}: {', '.join(r)}\n"

    def _commits_text(self):
        if not self.commits:
            return ""

        r = set([generate_repo_link(event) for event in self.commits])
        num_commits = sum([event["payload"]["distinct_size"] for event in self.commits])
        return (
            f">:arrow_up: {num_commits} {commit_form(num_commits)} to "
            f"{len(r)} {repo_form(len(r))}: {', '.join(r)}\n"
        )

    def _starred_repos_text(self):
        if not self.starred_repos:
            return ""

        r = [generate_repo_link(event) for event in self.starred_repos]
        return f">:star: {len(r)} {repo_form(len(r))}: {', '.join(r)}\n"


def generate_repo_link(event):
    repo_url = event["repo"]["url"]
    repo_url = repo_url.replace(
        "https://api.github.com/repos/", "https://www.github.com/"
    )
    repo_name = event["repo"]["name"]
    return f"<{repo_url}|{repo_name}>"


def generate_issue_link(event):
    issue_url = event["payload"]["issue"]["html_url"]
    issue_number = event["payload"]["issue"]["number"]
    repo_name = event["repo"]["name"]
    return f"<{issue_url}|{repo_name}#{issue_number}>"


# Singular or Plural Form in Summary
commit_form = lambda n: gettext.ngettext("commit", "commits", n)  # noqa
issue_form = lambda n: gettext.ngettext("issue", "issues", n)  # noqa
pr_form = lambda n: gettext.ngettext("PR", "PRs", n)  # noqa
release_form = lambda n: gettext.ngettext("release", "releases", n)  # noqa
repo_form = lambda n: gettext.ngettext("repo", "repos", n)  # noqa
