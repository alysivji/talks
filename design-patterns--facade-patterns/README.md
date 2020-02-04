# Design Patterns: Facade Pattern

## Talk Description

Developers spend lots of time writing code to integrate third-party packages and APIs into our project. Directly adding dependencies into business logic couples our code to something we do not control. This makes code hard to modify and even harder to test. Changes made to upstream packages require us to update integration code across the project.

This talk demonstrates HOWTO use Object-Oriented programming principles, specifically abstraction and encapsulation, to hide complexity and isolate the impact of changes. By using an API version upgrade as our guiding example, we will: walk through the initial implementation, discuss its limitations, and show how the Facade Pattern improves software design.

The session is geared towards developers of all levels looking for a friendlier approach to Design Patterns. By applying the principles outlined, you will be able to use the Facade pattern to write robust code that is easy to maintain.

## Media

- [Slides](http://bit.ly/facade-pattern)

## Development Environment

1. Create a virtual environment for Python 3.6+
1. `pip install -r requirements.txt`
1. [Set up a GitHub Personal Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
1. Set `GITHUB_OAUTH_TOKEN` environment variable to access token from previous step
