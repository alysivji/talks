# GitHub CHANGELOG Example

This folder contains code and tests used to demonstrate
the advantages of using the Facade Pattern
to wrap third-party APIs.

#### Table of Contents

<!-- TOC -->

- [Background](#background)
  - [MVP](#mvp)
- [Explaination of Code](#explaination-of-code)
  - [Directly Integrate with Requests](#directly-integrate-with-requests)
  - [Functions to Improve Readability](#functions-to-improve-readability)
  - [Implement Facade](#implement-facade)
  - [Utilize Sessions](#utilize-sessions)
  - [VCR.py Integration Tests](#vcrpy-integration-tests)
  - [GraphQL API](#graphql-api)
  - [PyGitHub](#pygithub)

<!-- /TOC -->

## Background

We want to generate a `CHANGELOG` for release.

### MVP

Command line application that takes arguments: `public repository` and `previous version`

- app grabs data from GitHub
- accepts a public repository and a previous release
- generate a CHANGELOG consisting of commit messages

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
Create a
[requests.session](https://requests.readthedocs.io/en/master/user/advanced/)
and use headers effectively.
Also use a GitHub token we can use
to grab information from private repos.

### VCR.py Integration Tests

> File: `e_vcr.py`

Replace responses-based unit tests
with VCR.py-based integration tests.

While we could use VCR.py for all of our tests,
I think it's better practice
to use it for integration tests around wrapper classes.
If underlying implementation changes,
we only have to worry about how it affects each Client library.

#### Need to reword

- when we create an issolated integration, we can add integration tests that hit the API directly
- something like VCR.py is useful when it is used to test the integration only
  - VCR.py to test all your logic will work, but your tests become dependent on an external thing you don't control, versus an interface you can

### GraphQL API

> File: `f_graphql.py`

GraphQL allows us to get the exact information we need.
Just by swapping out the adapter and adapter tests,
we can use a different kind of API
without having to change underlying code.

Integrating directly couples our code
to something we do not control.

### PyGitHub

> File: `g_pygithub.py`

There are Python-based GitHub wrappers available on PyPI,
but using them means are depending on code we didn't write.

Always be safe and wrap your integration code.
