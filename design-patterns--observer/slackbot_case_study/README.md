# Observer Pattern Case Study: Slackbot

This folder contains code and tests used to demonstrate best practices with the Observer Pattern.

#### Table of Contents

<!-- TOC -->

- [Project Introduction](#project-introduction)
- [Implementations](#implementations)
  - [MVP](#mvp)
  - [Dictionary Dispatch](#dictionary-dispatch)
  - [Event Emitter](#event-emitter)
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

Handlers for each of the commands are inlined within conditional blocks, one command per block. This is how I would initially solve the problem -- it's a solution that works and keeps things simple.

The issue with this approach is that our code is tightly coupled, i.e. business logic and web request handling logic are intertwined. This could become hard to manage as:
- we increase the number of commands we have to handle
- the business logic inside our command handler grows complex

### Dictionary Dispatch

Each command handler has it's own function. We create a dictionary with the key being the command and the value being a reference to the command handler function.

With this approach, our components are loosely coupled. We also removed the conditional, which is always a good thing.

We are on the right track, but there is a better way of registering handler functions with commands (ala Flask URL routing).

### Event Emitter

Created an abstraction, `EventEmitter`, that lets us register commands with different function handlers using a decorator. This design results in loosely coupled components.

In our use case, there is a one-to-one relationship between command (state) and function handler (observers). This has been taken into account in the `EventEmitter` class.

If we need to to have a one-to-many relationship between state and observers, we can use [pyee](https://pyee.readthedocs.io/en/latest/).

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
    - Request URL: `URL exposed via ngrok` (will be different every time you start a ngrok process)
    - Short Description: `Observer Pattern Demo App`
1. Click `Save`
1. In app dashboard, click `Basic Information` > `Install to Workspace` > `Allow`

The app is now installed into your Slack workspace. You can interact with it via the `/observer` command.
