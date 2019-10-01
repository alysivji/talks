# If Statements are a Code Smell

## Length

30

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

`if` statements allow us to selectively execute code based on conditional logic. Overusing conditionals produces code that is hard to read and difficult to modify. This talk will demonstrate HOWTO refactor `if` statements into polymorphic classes, resulting in cleaner program design. After this session, you will be able to implement complex conditional logic using simple Python classes.

## Who and Why (Audience)

> 1–2 paragraphs that should answer three questions: (1) Who is this talk for? (2) What background knowledge or experience do you expect the audience to have? (3) What do you expect the audience to learn or do after watching the talk

The session is geared towards developers who do not have a lot of experience implementing Object-Oriented solutions. After this talk, you will be able to identify situations where Object-Oriented principles can be used to simplify complex conditional logic. Using the steps outlined, you will be able to refactor code to improve software design without changing existing functionality.

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

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed here: https://bit.ly/siv-talks-playlist
