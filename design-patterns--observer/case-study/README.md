# Observer Pattern Case Study: Slackbot

This folder contains code and tests used to demonstrate best practices with the Observer Pattern.

#### Table of Contents

<!-- TOC -->

- [Project Introduction](#project-introduction)
- [Implementations](#implementations)
  - [MVP](#mvp)
- [Setup Development Environment](#setup-development-environment)
  - [Install Dependencies](#install-dependencies)
  - [Setting up bot in Slack Workspace](#setting-up-bot-in-slack-workspace)

<!-- /TOC -->

## Project Introduction

We will create a Slack application that responds to innovations via the [slash command](https://api.slack.com/interactivity/slash-commands).

How do Slash commands work?
url encoded form data

We will set up a flask endpoint to blah blah blah

## Implementations

There are various implementations of Slackbot to

### MVP

Use conditional branches to

## Setup Development Environment

We will need to install dependencies and create

Requires:

- Slack workspace for bot testing
  - [create a new workspace](https://slack.com/help/articles/206845317-Create-a-Slack-workspace)
- [ngrok](https://ngrok.com/) installed on your development machine
  - exposes our local server to simplify bot testing

### Install Dependencies

1. Create a virtual environment for Python 3.9
1. `make install`

- Start server: `make inlined-solution`
- Expose local server: `make ngrok`
  - terminal session contains public URL for exposed server

### Setting up bot in Slack Workspace

#### Create new Slack application

1. Go to https://api.slack.com/apps
1. Click `Create New App` > `From scratch`
    - App Name: Observer Pattern Demonstration App
    - Pick workspace to develop the app in
1. Click `Create App`

This will be the application we use for testing purposes.

#### Create Slash Command

1. Goto https://api.slack.com/apps > Select App
1. In app dashboard, click `Slack Commands` > 'Create New Command`
    - Command: `/observer`
    - Request URL: `URL exposed via ngrok`
    - Short Description: `Observer Pattern Demo App`
1. Click `Save`
1. In app dashboard, click `Basic Information` > `Install to Workspace` > `Allow`

The app is now installed into your Slack workspace. You can interact with it via the `/observer` command.
