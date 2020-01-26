# GitHub Summary Example

This folder contains code and tests used to demonstrate
the use of conditional logic versus polymorphic classes.

## Background

The Chicago Python Slack workspace
has a [bot](https://github.com/busy-beaver-dev/busy-beaver)
that posts daily summaries of public GitHub activity for registered users.

[GitHub's API](https://developer.github.com/v3/) allows us
to view [all public events](https://developer.github.com/v3/activity/events/#list-public-events)
for a given user. The bot pulls events from the API, collects events by type,
and generates summary output for each user.

## Setting Up Environment

1. [Set up a GitHub Personal Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
1. Set `GITHUB_OAUTH_TOKEN` environment variable to access token from previous step
1. `pip install -r requirements.txt`

## Explaination of Code

### Overview of Files

- `a` is MVP
- `b` is trying to change MVP, it's slightly painful and a bit messy
- `c` is stage 1 of the refactor
- `d` is what it looks like after the refactor is complete
- `e` shows how easy it is to make changes by adding a class (Single Responsibility Principle FTW)
- `f` is the final version from production

### Conditional Logic

#### MVP

When we first attack this problem, it makes sense to do it sequentially:

- use requests to fetch data from the GitHub API, see [`toolbox.py`](toolbox.py)

[TODO]
