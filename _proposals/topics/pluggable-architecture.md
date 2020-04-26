# Pluggable Architecture

## Length

30

## Audience Level

All

## Elevator Pitch

Plugins are everywhere - in web browsers, text editors, and web frameworks. We use plugins to customize functionality of existing software, but have you ever designed a plugin from scratch? This talk examines Pluggable Architecture by creating a custom plugin system. After this session, will be able to extend the functionality of your favorite library without modify existing code.

## Description

Applications and libraries with pluggable architecture allow developers to customize software without having to modify existing code. We can use plugins to modify user interfaces, create new workflows, and interface with legacy systems. Designing a plugin is often difficult - documentation is sparse, outdated, or non-existent. You end up diving into an unfamiliar codebase to figure out what to do.

This talk examines Pluggable Architecture by creating a custom plugin system: we will design an interface, think about where to hook in custom behavior, and discuss testing techniques. Understanding these principles will enable us to write custom plugins for third-party packages. Extend the functionality of your favorite library without touching existing code!

### Outline

Introduction to topic and speaker (2 minutes)

Overview of Plugin Architecture (3 minutes)
  - What is a plugin
  - Examples in applications and libraries
  - Advantages / disadvantages

Motivating Example: Extend functionality of an existing library (5 minutes)
  - Want to auto-generate API documentation for the Falcon web framework
  - Existing library doesn't support Falcon
  - Use hooks to add new functionality

Designing a Pluggable Interface (7 minutes)
  - From the application's perspective
  - How / when should plugins interface with application logic
  - Walkthrough class diagram and interactions
  - Aside: Design Patterns provide a blueprint

Plugin Architecture in the Wild (5 minutes)
  - Overview of popular Python libraries with pluggable architecture
  - Brief description of how they are designed

Writing a Plugin: Things to Think About (5 minutes)
  - How to write a custom plugin
  - Testing tips
  - Aside: Continuous Integration testing matrix

Conclusion (3 minutes)
  - Overview of Pluggable Architecture
  - Add functionality without touch existing code

## Notes

While this will be my first time presenting this talk, I have written a [blog post on Pluggable Architecture](https://alysivji.github.io/simple-plugin-system.html). This post was feature in PyCoders Weekly.

I have experience in breaking down complex concepts into easily understood components. I recently gave a talk on how if statements can be refactored into polymorphic classes at PyCon US. The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

## Tags

Python, object oriented programming, oop, software design, refactoring, software architecture, classes
