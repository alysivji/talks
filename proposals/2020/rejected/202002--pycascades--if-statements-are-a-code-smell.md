# If Statements are a Code Smell

## Length

25

## Audience Level

All

## Elevator Pitch

`if` statements allow us to selectively execute code based on conditional logic. Overusing conditionals results in code that is hard to understand and difficult to modify. This talk will demonstrate how to refactor `if` statements into polymorphic classes, resulting in cleaner program design.

## Description

Writing software is about making trade-offs between getting things done and doing them right. Time constraints often force us to take shortcuts to handle slight variations resulting in patches of conditional logic sprinkled throughout our codebase. Workarounds that once allowed us to move quickly now hinder our progress in getting new features out to customers. It doesn't have to be this way!

This talk will demonstrate how to use Object-Oriented programming principles, specifically polymorphism, to handle conditional logic resulting in code that is easy to modify. The material will be presented in the context of a real-world code refactor for an open-source project. We will examine the initial solution, discuss its limitations, and walk through the process of refactoring duplicate `if` blocks into polymorphic classes.

The session is geared towards developers who do not have a lot of experience implementing Object-Oriented solutions. After this talk, you will be able to identify situations where Object-Oriented design can be used to simplify complex conditional logic. Using the steps outlined, you will be able to refactor code to improve software architecture without changing existing functionality.

### Outline

- Introduction to topic and speaker (2 minutes)
    - Not here to attack individuals or their code
    - Want to share a pattern that has helped my code become more readable and more testable
- Overview of `if` statements (3 minutes)
    - What is an `if` statement?
    - Walk thru Python examples
    - What makes code hard to read and difficult to modify?
    - Code smells are things we MIGHT need to look into
- Code Smell #1: Compound `if` Statement (2 minutes)
    - Discuss limitations + how to refactor
- Code Smell #2: Nested `if` Statements (3 minutes)
    - Discuss limitations + how to refactor
- Code Smell #3: Duplicate `if` Statements (3 minutes)
    - Introduction to problem with an open-source case study
    - Initial solution (hackathon)
    - Try to add a new feature, it's difficult
    - Discuss limitations
- Object-Oriented Programming (OOP) in Python (5 minutes)
    - High-level intro
    - Principles of OOP
    - Dive into polymorphism with detailed example
- Duplicate `if` Statements: Case Study Revisited (5 minutes)
    - Break the problem down -- what are we trying to do
    - Walk thru refactor process
    - Explicitly define steps to refactor `if` statements into polymorphic classes
    - Add new feature with ease
- Closing (2 minutes)
    - `if` statements: benefits vs tradeoffs
    - Review steps to refactor `if` statements into polymorphic classes
    - Shoutout to testing
    - Shoutout to learning by developing open-source software

## Notes

I have presented this talk at PyOhio, PyCon Balkan, and a local Python meetup (Chicago Python). The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed here: https://bit.ly/siv-talks-playlist

## Tags

Python, object oriented programming, oop, software design, refactoring, classes
