# Pluggable Architecture

## Bio

Aly Sivji is a Canadian expat living in Chicago. By day, he builds backend systems at Numerator. By night, he is a co-organizer of the Chicago Python Users Group (ChiPy). Aly is an active participant in the ChiPy Mentorship Program and he loves helping intermediate developers become experts. Outside of Python, Aly enjoys cycling, reading, and rewatching old TV shows.

## Twitter URL

https://twitter.com/CaiusSivjus

## Personal Website URL

https://www.alysivji.com

## Linkedin URL

https://www.linkedin.com/in/alysivji/

## Github URL

https://github.com/alysivji/

## Audience Level

Intermediate

## Talk Length

25

## Who should attend

The session is geared towards intermediate developers looking to understand how Object-Oriented Design Patterns can be used to build modular systems.

## Brief Description

Plugins are everywhere - in web browsers, text editors, and web frameworks. We use plugins to customize functionality of existing software, but have you ever designed a plugin from scratch? This talk examines Pluggable Architecture by creating a custom plugin system. After this session, will be able to extend the functionality of your favorite library without modify existing code.

## Detailed Abstract

Applications and libraries with pluggable architecture allow developers to customize software without having to modify existing code. We can use plugins to modify user interfaces, create new workflows, and interface with legacy systems. Designing a plugin is often difficult - documentation is sparse, outdated, or non-existent. You end up diving into an unfamiliar codebase to figure out what to do.

This talk examines Pluggable Architecture by creating a custom plugin system: we will design an interface, think about where to hook in custom behavior, and discuss testing techniques. Understanding these principles will enable us to write custom plugins for third-party packages. Extend the functionality of your favorite library without touching existing code!

### Outline

Introduction to topic and speaker (2 minutes)

Overview of Plugin Architecture (2 minutes)
- What is a plugin
- Examples in applications and libraries
- Advantages / disadvantages

Motivating Example: Extend functionality of an existing library (4 minutes)
- Want to auto-generate API documentation for the Falcon web framework
- Existing library doesn't support Falcon
- Use hooks to add new functionality

Designing a Pluggable Interface (6 minutes)
- From the application's perspective
- How / when should plugins interface with application logic
- Walkthrough class diagram and interactions
- Aside: Design Patterns provide a blueprint

Plugin Architecture in the Wild (5 minutes)
- Overview of popular Python libraries with pluggable architecture
- Brief description of how they are designed

Writing a Plugin: Things to Think About (4 minutes)
- How to write a custom plugin
- Testing tips
- Aside: Continuous Integration testing matrix

Conclusion (2 minutes)
- Overview of Pluggable Architecture
- Add functionality without touch existing code

## What will attendees learn

Using the steps outlined in this talk, attendees will understand how to approach writing custom plugins for their favourite third-party libraries.

Attendees looking to learn how to build applications with a plugin system will be presented a scaled-down example with links for further reading.

## Previous Presentation Experience / History

Will be giving this talk at Python Web Conf 2020 in June. I have also written a blog post on Pluggable Architecture that was featured in PyCoders Weekly: https://alysivji.github.io/simple-plugin-system.html

I have experience in breaking down complex concepts into easily understood components. I recently gave a talk on how if statements can be refactored into polymorphic classes at PyCon Balkan. The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyTexas, PyOhio, and led a 3-hour tutorial at PyCon US.

## URL(s) to Previous Presentations

https://bit.ly/siv-talks-playlist

## Tags

Python, object oriented programming, oop, software design, refactoring, software architecture, classes
