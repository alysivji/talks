# If Statements are a Code Smell

## Length

30

## Audience Level

Beginner

## Elevator Pitch

`if` statements allow us to control what statements are executed. Code with too many `if` statements is hard to read and even harder to change. This talk will demonstrate how to refactor complex conditional logic with simple Python classes using a real-world example of Object-Oriented design.

## Description

`if` statements are elements of a programming language that allow us to control what statements are executed. By chaining together a series of `if` statements, we can solve any problem we can think of. But code with too many `if` statements is hard to read and even harder to change. Workarounds that once allowed us to move fast, now get in the way when we go in to make modifications. It doesn’t have to be this way!

This talk demonstrates HOWTO handle complex conditional logic with simple Python classes. The material will be presented in the context of a code refactor for an open-source project: we examine the initial solution featuring duplicate `if` statements, show how hard it is to make a change, and walk through the process of refactoring `if` blocks into polymorphic classes. The case study has been simplified to illustrate concepts you can apply to your own code.

The session is geared towards beginner / intermediate developers who do not have a lot of experience designing Object-Oriented solutions. After this talk, you will be able to identify situations where Object-Oriented principles can be used to simplify complex conditional logic. Using the steps outlined, you will be able to refactor code to improve software design without changing existing functionality.

### Outline

- Introduction to topic and to speaker (2 minutes)
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
- Code Smell #3: Duplicate `if` Statements (6 minutes)
    - Introduction to problem with an open-source case study
    - Initial solution (hackathon)
    - Try to add a new feature, it's difficult
    - Discuss limitations
- Object-Oriented Programming (OOP) in Python (6 minutes)
    - High-level intro
    - Principles of OOP
    - Dive into polymorphism with detailed example
- Duplicate `if` Statements: Case Study Revisited (6 minutes)
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

I have presented this talk at PyCon US, PyCon Balkan,and PyOhio. The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyTennessee, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed here: https://bit.ly/siv-talks-playlist

## Slides link (optional)

[http://bit.ly/code-smell-if-statements](http://bit.ly/code-smell-if-statements)
