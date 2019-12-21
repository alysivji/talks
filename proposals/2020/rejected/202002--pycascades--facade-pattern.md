# Everyday Design Patterns: Facade Pattern

## Length

25

## Audience Level

All

## Elevator Pitch

Developers spend lots of time writing code to integrate with third-party packages and APIs. We spend additional time updating systems when the services we depend on change. This talk will demonstrate HOWTO leverage the Facade Pattern to hide complexity and isolate the impact of changes.

## Description

Whether we realize it or not, we are making software design decisions when we integrate third-party libraries and APIs into our codebase. Directly integrating dependencies into business logic results in code that is brittle and difficult to modify. Changes made to upstream packages can require us to update integration code across the project.

This talk will demonstrate how to use Object-Oriented programming principles, specifically abstraction and encapsulation, to isolate the impact of upstream changes. The material will be presented in the context of modifying code to handle an API version upgrade. First, we will walk through the initial implementation and discuss its limitations. Then we will investigate how the Facade Pattern can improve program design.

The session is geared towards developers of all levels looking for a friendlier approach to Design Patterns. By applying the principles outlined in this talk, you will be able to utilize the Facade pattern to write robust code that is easier to maintain.

### Outline

- Introduction to topic and speaker (2 minutes)
- Design Patterns Introduction (3 minutes)
    - What are design patterns?
    - Benefits of patterns
    - Types of Patterns: Creational, Structural, Behavioral
- Case Study: Interacting with APIs (5 minutes)
    - Introduce problem -- downloading data from 3rd party API
    - Walk thru initial solution (direct integration)
    - API changes...!!! Changing our code is painful!
    - Aside: tests are complicated to write
- Object-Oriented Programming (OOP) (5 minutes)
    - High-level intro
    - Principles of OOP
    - Dive into encapsulation and abstraction
    - Encapsulation and abstraction in Python
- Case Study Revisited: Facade Pattern (8 minutes)
    - Adding a layer between the API and implementation enables changes to be isolated
    - Walk through the process of changing code to support new API
    - Show how facade pattern simplifies testing with fakes
    - Other examples of Facade pattern in practice: wrap Python libraries
- Closing (2 minutes)
    - Benefits of Design Patterns
    - Program to an interface, not an implementation
    - Don't get too hung up on diagrams and terminology
    - Focus on understanding the problem you are trying to solve

## Notes

While it will be my first time giving this talk in its entirety, I gave a short lightning talk about the Facade Pattern at a Chicago Python meetup. The experience helped me understand how to structure the various topics to make the material digestible.

I have experience in breaking down complex concepts into easily understood components. I recently gave a talk on how if statements can be refactored into polymorphism classes at PyCon Balkan. The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

## Tags

Python, object oriented programming, oop, software design, refactoring, software architecture, classes
