# Everyday Design Patterns: Facade Pattern

## Subtitle

> Juice up your title with max. 100 chars, e.g. "Interactively visualize big data with high performance."

Make your code easy to change -- code to interfaces, not implementations.

## Abstract (Longer Version)

> Description of the session proposal you are submitting. Be sure to include the goals and any prerequisite required to fully understand it. See the section Submitting Your Talk, Trainings, Helpdesk or Poster of the CFP for further details.

Developers spend lots of time wiring third-party packages and APIs into our project. Directly integrating dependencies into business logic couples our code to something we do not control. This makes code hard to modify and even harder to test. Changes made to upstream packages require us to update integration code across the project.

This talk demonstrates HOWTO use Object-Oriented programming principles to hide complexity and isolate the impact of changes. By using an API version upgrade as our guiding example, we will: walk through a tightly coupled implementation, discuss its limitations, and show how the Facade Pattern improves software design.

The session is geared towards developers of all levels looking for a friendlier approach to Design Patterns. By applying the principles outlined, you will be able to use the Facade pattern to write robust code that is easy to maintain.

### Outline

Introduction to topic and speaker (2 minutes)

Design Patterns Introduction (3 minutes)
- What are design patterns?
- Benefits of patterns
- Criticism of Patterns

Facade Pattern (5 minutes)
- High-level overview
- Facade Pattern in Python
- Use functions to hide implementation details
- Limitations of functions

Case Study: GitHub Changelog (5 minutes)
- Introduce problem -- downloading data from GitHub API
- Walkthrough initial solution (direct integration)
- Changing our code is painful!
- Aside: tests are complicated to write

Object-Oriented Programming (OOP) (5 minutes)
- High-level intro
- Principles of OOP
- Dive into encapsulation with code example
- Dive into abstraction with code example

Case Study Revisited: Facade Pattern (8 minutes)
- Walk through implementation (code and diagram)
- Show how to use new GitHub integration
- Result is loosely coupled modules
- Walkthrough the process of changing code to support GraphQL API (with short GraphQL primer)
- Show how facade pattern simplifies testing with stubs

Closing (2 minutes)
- Benefits of Design Patterns
- Program to an interface, not an implementation
- Focus on understanding the problem you are trying to solve

## Abstract (short version)

> We need a short description e.g. for YouTube and other distribution channels with limited space for abstracts. You could just use a shorter version of the long abstract.

Directly integrating dependencies into business logic couples our code to something we do not control. Changes made to upstream packages require us to update integration code across the project. This talk demonstrates how the Facade pattern can improve software design and simplify testing.

## Prerequisites for attending the session

> What should attendees be familiar with already, important for intermediate and advanced talks.

functions, classes

## Python Skill level

> How experienced should the audience be in python

Beginner

## Domain Expertise

> The domain expertise your audience should have to follow along (e.g. how much should one know about DevOps or Data Science already)

Beginner

## Tags

Abstractions, Best Practice, Clean Code, Development, Software Design

## Notes

I have given at a local User Group (Chicago Python) and PyTennessee. The audience appreciated the use of a real-world code example to help solidify abstract Software Design concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyCon Balkan, PyOhio, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist
