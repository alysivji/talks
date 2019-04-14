from datetime import timedelta

from busy_beaver.adapters.github import GitHubAdapter
from busy_beaver.adapters.utilities import subtract_timedelta  # noq
from busy_beaver.config import oauth_token

github = GitHubAdapter(oauth_token)

boundary_dt = subtract_timedelta(timedelta(days=1))


def recent_activity_text(user):
    activity = github.user_activity_after(user, boundary_dt)

    events_of_interest = []
    for event in activity:
        if event['type'] in ['PushEvent', 'WatchEvent']:
            event_of_interest = {}
            event_of_interest['type'] = event['type']
            event_of_interest['repo'] = f"<{event['repo']['url']}|{event['repo']['name']}>"

            if event['type'] == 'PushEvent':
                event_of_interest['commit_count'] = len(event['payload']['commits'])

            events_of_interest.append(event_of_interest)

    if len(events_of_interest) > 1:
        text = f"<@{user}> as <https://github.com/GitUser|GitUser>\n"
        for event_type in sorted(list(set([e['type'] for e in events_of_interest]))):
            events = [event for event in events_of_interest if event['type'] == event_type]
            repos = list(set([event['repo'] for event in events]))
            repo_count = len(repos)

            if repo_count > 1:
                repo_s = "s"
            else:
                repo_s = ""

            if event_type == 'PushEvent':
                commit_count = sum([event['commit_count'] for event in events])
                if commit_count > 1:
                    commit_s = "s"
                else:
                    commit_s = ""
                text += (
                    f">:arrow_up: {commit_count} commit{commit_s} to "
                    f"{repo_count} repo{repo_s}: {', '.join(repos)}\n"
                )
            if event_type == 'WatchEvent':
                text += f">:star: {repo_count} repo{repo_s}: {', '.join(repos)}\n"
        text += "\n"
    else:
        text = ""

    return text
