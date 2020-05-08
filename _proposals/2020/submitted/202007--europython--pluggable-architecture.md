# Pluggable Architecture

## Subtitle

> Juice up your title with max. 100 chars, e.g. "Interactively visualize big data with high performance."

Extend functionality without touching existing code

## Abstract (Longer Version)

> Description of the session proposal you are submitting. Be sure to include the goals and any prerequisite required to fully understand it. See the section Submitting Your Talk, Trainings, Helpdesk or Poster of the CFP for further details.

Applications and libraries with a pluggable architecture allow developers to add custom functionality. Plugins can customize user interfaces, create new workflows, and interface with legacy systems. Designing a plugin is often difficult - documentation is sparse, outdated, or non-existent. You end up diving into a unfamiliar codebase to figure out what to do.

This talk examines Pluggable Architecture by creating a custom plugin system: we will design an interface, think about where to hook in custom behavior, and discuss testing techniques. Understanding these principles will enable us to write custom plugins for third-party libraries. Extend the functionality of your favourite library without touching existing code!

### Outline

Introduction to topic and speaker (2 minutes)

Overview of Plugin Architecture (3 minutes)
  - What is a plugin
  - Examples in applications and libraries
  - Advantages / disadvantages

Motivating Example: Extend functionality of an existing library (5 minutes)
  - Want to auto-generate API documentation
  - Existing library doesn't support our framework
  - Use hooks to add new functionality

Designing a Pluggable Interface (7 minutes)
  - From the application's perspective
  - How / when should plugins interface with application logic
  - Walkthrough class diagram and interactions
  - Aside: Design Patterns provide a blueprint

Plugin Architecture in the Wild (5 minutes)
  - Overview of popular Python libraries with pluggable architecture
  - Brief description of how they are designed

Writing a Plugin: Things to Think About (7 minutes)
  - How to write a custom plugin
  - Testing tips
  - Aside: Continuous Integration testing matrix

Conclusion (3 minutes)
  - Overview of Pluggable Architecture
  - Add functionality without touch existing code

## Abstract (short version)

> We need a short description e.g. for YouTube and other distribution channels with limited space for abstracts. You could just use a shorter version of the long abstract.

Applications and libraries with a pluggable architecture allow developers to add custom functionality. Designing a plugin is often difficult - documentation is sparse, outdated, or non-existent. You end up diving into a unfamiliar codebase to figure out what to do. This talk examines Pluggable Architecture by designing a custom plugin system. Extend the functionality of your favourite library without touching existing code!

## Prerequisites for attending the session

> What should attendees be familiar with already, important for intermediate and advanced talks.

functions, classes

## Python Skill level

> How experienced should the audience be in python

Intermediate

## Domain Expertise

> The domain expertise your audience should have to follow along (e.g. how much should one know about DevOps or Data Science already)

Beginner

## Tags

- Abstractions
- Architecture
- Development
- Software Design
- System Architecture

## Notes

While this will be my first time presenting this talk, I have written a [blog post on Pluggable Architecture](https://alysivji.github.io/simple-plugin-system.html). This post was feature in PyCoders Weekly.

I have experience in breaking down complex concepts into easily understood components. I recently gave a talk on how if statements can be refactored into polymorphic classes at PyCon Balkan. The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist
