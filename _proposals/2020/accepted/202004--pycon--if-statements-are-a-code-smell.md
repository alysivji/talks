# If Statements are a Code Smell

## Length

30

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

`if` statements are elements of a programming language that allow us to control what statements are executed. By chaining together a series of `if` statements, we can solve any problem we can think of. But code with too many `if` statements is hard to read and even harder to change. Workarounds that once allowed us to move fast, now get in the way when we go in to make modifications. It doesn’t have to be this way!

This talk demonstrates HOWTO handle complex conditional logic with simple Python classes. The material will be presented in the context of a code refactor for an open-source project: we examine the initial solution featuring duplicate `if` statements, show how hard it is to make a change, and walk through the process of refactoring `if` blocks into polymorphic classes. The case study has been simplified to illustrate concepts you can apply to your own code.

After this talk, you will be able to identify situations where an object-oriented solution can be used to improve software design. You will also be exposed to tradeoffs we need to think about before refactoring to higher-level abstractions.

## Who and Why (Audience)

> 1–2 paragraphs that should answer three questions: (1) Who is this talk for? (2) What background knowledge or experience do you expect the audience to have? (3) What do you expect the audience to learn or do after watching the talk

The session is geared towards beginner / intermediate developers who do not have a lot of experience designing Object-Oriented solutions. After this talk, you will be able to identify situations where Object-Oriented principles can be used to simplify complex conditional logic. Using the steps outlined, you will be able to refactor code to improve software design without changing existing functionality.

### Outline

> The “outline” is a skeleton of your talk that is as detailed as possible, including rough timings or estimates for different sections. If requesting a 45 minute slot, please describe what content would appear in the 45 minute version but not a 30 minute version, either within the outline or in a paragraph at the end.

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

## Additional Notes

> Anything else you would like to share with the committee:
> Speaker public speaking experience.
> Speaker subject matter experience.
> Have the speaker(s) given this presentation before elsewhere?
> Links to recordings, slides, blog posts, code, or other material.
> Specific needs or special requests — accessibility, audio (will you need to play pre-recorded sound?), or restrictions on when your talk can be scheduled.

I have presented this talk at PyOhio, PyCon Balkan, and a local Python meetup (Chicago Python). The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyTennessee, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed here: https://bit.ly/siv-talks-playlist
