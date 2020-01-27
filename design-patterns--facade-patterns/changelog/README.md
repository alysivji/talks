# GitHub CHANGELOG Example

This folder contains code and tests used to demonstrate
the advantages of using the Facade Pattern
to wrap third-party APIs.

#### Table of Contents

<!-- TOC -->

- [Background](#background)
  - [MVP](#mvp)
- [Development Environment](#development-environment)
- [Explaination of Code](#explaination-of-code)
  - [Directly Integrate with Requests](#directly-integrate-with-requests)
  - [Functions to Improve Readability](#functions-to-improve-readability)
  - [Implement Facade](#implement-facade)
  - [Utilize Sessions](#utilize-sessions)
  - [Tests](#tests)

<!-- /TOC -->

## Background

We want to generate a `CHANGELOG` for release.

### MVP

Command line application that takes arguments: `public repository` and `previous version`

App grabs data from GitHub and

 takes in a public repository,
a previously tagged release,

Generate a CHANGELOG consisting of commit messages

## Development Environment

1. Create a virtual environment for Python 3.6+
1. `pip install -r requirements.txt`
1. [Set up a GitHub Personal Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
1. Set `GITHUB_OAUTH_TOKEN` environment variable to access token from previous step

## Explaination of Code

### Directly Integrate with Requests

> File: `a_use_requests.py`

Use requests to hit endpoints
and collect information.

For tests we use responses to mock out
the external API call.
Tests depend on GitHub API implemtnation,
i.e. something we do not control.

If the API changes,
we have to modify our code AND tests.
Basically rewrite everything again
to ensure it works as expected.

This code is also hard to read,
we have to read thru each line to
understand what's going on.

### Functions to Improve Readability

> File: `b_functions.py`

Split up the `generate_changelog()` function
to make it more readable.
We can unit test each of the functions separately.

Monkeypatch the smaller functions to unit test
`generate_changelog()`.

We can test our business logic with a value
and test the integration code separately.

### Implement Facade

> File: `c_facade.py`

Created a wrapper around the GitHub API.
Monkeypatch the GitHubClient with
a FkeGitHubClient stub to simplify tests.

### Utilize Sessions

> File: `d_session.py`

Everything is encapsulated in a class
that can hold state.
Create a [requests.session](https://requests.readthedocs.io/en/master/user/advanced/)
and use headers effectively.
Also use a GitHub token we can use
to grab information from private repos.

### Tests

> File:

- add integration test with vcr.py
