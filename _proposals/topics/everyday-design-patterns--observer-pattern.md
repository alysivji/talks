# Everyday Design Patterns: Observer Pattern

## Length

25

## Audience Level

Intermediate

## Elevator Pitch

The Observer Pattern enables us to design event-driven systems using loosely coupled components. In this talk, we will learn how, when, and why to use this pattern; we will explore how popular PyPI packages use the pattern; and, we will design a decorator-based Observer to process Slack events.

## Description

Design Patterns are solutions to commonly occurring problems in Software Design. The Observer Pattern is a popular pattern that enables us to design event-driven systems using loosely coupled components. This pattern is widely used in the Python ecosystem: we find implementations in the standard library and in packages such as Django and Flask.

This talk will dive deep into the Observer Pattern. We will start with a high-level overview of how, when, and why to use the pattern. Next, we will examine various Python implementations of this pattern. Finally, we will create a decorator-based Observer to dynamically dispatch events received from Slack webhooks.

This session is geared towards intermediate and advanced developers looking for a friendly and practical approach to Design Patterns. By applying the principles outlined, you will be able to use the Observer Pattern to create loosely coupled components that are easy to modify and even easier to test.

### Outline

- Introduction to topic and speaker (2 minutes)
- What are design patterns? (1 minutes)
    - solution to a commonly occurring problem in software design
- Observer Pattern (5 minutes)
    - High-level overview -- how, when, and why to use the pattern
    - Benefits / Tradeoffs
    - Observer Pattern in Python with classes
    - Observer Pattern in Python with decorators
    - Observer Pattern versus Pub/Sub
- Observer Pattern in the Wild (5 minutes)
    - Standard Library: Logging, Tkinter
    - Flask: route decorators, exception handlers
    - Django signals
    - PursuedPyBear event-driven architecture
    - Front-end DOM programming
    - Note that these implementations are slightly different
    - Design Patterns are not cookiecutter solutions, they should be adapted to solve the specific problem you have
- Case Study: Slack Webhook (10 minutes)
    - Introduce problem -- set up a Slackbot that sends events to a webhook
    - Walkthrough initial solution: if statements checking for an event type and then performing an action
    - This gets out of hand as we add more events/actions; code is hard to read and tests become unmanageable
    - Refactor to a decorator-based implementation from earlier; looks and feels Pythonic
    - Aside: we just implemented node.js `EventEmitter` with decorators
    - Aside: `pyee` library is a Python port of `EventEmitter`; can plug into async event loops (both: asyncio and twisted)
- Closing (2 minutes)
    - Observer Pattern helps us design software that is loosely coupled
    - While implementations of the observer pattern are slightly different, they share the same building blocks
    - The important thing about Design Patterns is that they provide a shared vocabulary. We communicate using higher-order abstractions, not low-level details
    - When somebody mentions something is implemented with an observer pattern, you know what this means even though you do not know how it is implemented
    - Takeaway: if you like something about a library, find out why. Digging deeper will help you learn about these patterns and improve your software design skills

## Notes

This will be my first time giving this talk. Because of this, I have estimated my outline at 25 minutes. If there is additional time, I plan to expand upon the *Aside* bullet points in the case study section.

I have experience in giving talks on applied Object-Oriented Principles. I have previously given a talk on how if statements can be refactored into polymorphic classes (PyCon 2020, PyCon Balkan 2019, PyOhio 2019). Also have given a talk on the Facade Design Pattern (PyTennessee 2020, PyTexas 2020).

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyCon Africa, EuroPython, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

## Tags

Python, object oriented programming, oop, software design, refactoring, software architecture, design patterns, patterns
