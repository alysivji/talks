# Everyday Design Patterns: Observer Pattern

## Length

25

## Audience Level

Intermediate

## Elevator Pitch

The Observer Pattern is widely used as it enables developers to write loosely coupled software that is easy to maintain. In this talk, we will dive deep into the Observer Pattern, examine various Python implementations, and design a decorator-based Observer that looks and feels Pythonic.

## Description

The Observer Pattern enables developers to write loosely coupled code that is easy to maintain. This pattern is widely used in the Python ecosystem: there are implementations in the standard library and in popular packages such as Django and Flask.

This talk will dive deep into the Observer Pattern. We will start with a high-level overview of the pattern. Next, we will examine various implementations of this pattern in the wild. Finally, we will create a decorator-based Observer to dispatch events sent from GitHub via webhooks.

The session is geared towards developers of all levels looking for a friendlier approach to Design Patterns. By applying the principles outlined, you will be able to use the Observer Pattern to create loosely coupled systems that are easy to modify and even easier to test.

### Outline

- Introduction to topic and speaker (2 minutes)
- What are design patterns? (1 minutes)
    - solution to a commonly occurring problem in software design
- Observer Pattern (5 minutes)
    - High-level overview
    - Benefits / Tradeoffs
    - Observer Pattern in Python with classes
      - seems a bit confusing tbh
    - Observer Pattern in Python with decorators
      - this is how you might encounter them in the wild
    - Observer Pattern versus Pub/Sub
- Observer Pattern in the Wild (5 minutes)
    - Standard Library: Logging, Tkinter
    - Flask: route decorators, exception handlers
    - Django signals
    - PursuedPyBear event-driven architecture
    - Front-end DOM programming
    - Note that these implementations are slightly different
    - Design Patterns are not cookiecutter solutions, they should be adapted to solve the specific problem you have
- Case Study: GitHub Webhook (10 minutes)
    - Introduce problem -- set up a GitHub webhook that posts messages to Slack
    - Walkthrough initial solution: if statements checking for an event type and then performing an action
    - This gets out of hand as we add more events/actions; code is hard to read and tests become unmanageable
    - Refactor to a decorator-based implementation from earlier
    - Aside: basic implementation of node's `EventEmitter`
    - Aside: `pyee` library does and can plug into async event loops (both: asyncio and twisted)
- Closing (2 minutes)
    - Observer Pattern helps us design software that is loosely coupled
    - While implementations of the observer pattern are slightly different, they share the same building blocks
    - The important thing about Design Patterns is that they provide a shared vocabulary. Our discussions focus on higher-order abstractions, not low-level details
    - When somebody mentions something is implemented with an observer pattern, you know what this means even though you do not know how it is implemented
    - Takeaway: if you like something about a library, find out why. Digging deeper will help you learn about these patterns and improve your design of software design

## Notes

This will be my first time giving this talk. Because of this, I have conservatively estimated my outline at 25 minutes. If there is additional time, I plan to expand upon the Aside bullet points in the case study section. Can definitely get another 5-15 minutes of material in line with the overall theme of the talk.

I have experience in giving talks on applied Object-Oriented Principles. I recently gave a talk on how if statements can be refactored into polymorphic classes (PyCon 2020, PyCon Balkan 2019, PyOhio 2019). Also have given a talk on the Facade Design Pattern (PyTennessee 2020, PyTexas 2020).

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyCon Africa, EuroPython, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

## Tags

Python, object oriented programming, oop, software design, refactoring, software architecture, design patterns, patterns
