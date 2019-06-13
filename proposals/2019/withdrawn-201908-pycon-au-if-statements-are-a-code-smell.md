# If Statements are a Code Smell

## Length

30

## Abstract

`if` statements allow us to selectively execute code based on conditional logic. Overusing conditionals results in code that is hard to understand and difficult to modify. This talk will demonstrate how to refactor `if` statements into polymorphic classes, resulting in cleaner program design.

## Description

Writing software is about making trade-offs between getting things done and doing them right. Time constraints often force us to take shortcuts to handle slight variations resulting in patches of conditional logic sprinkled throughout our codebase. Workarounds that once allowed us to move quickly now hinder our progress in getting new features out to customers. It doesn't have to be this way!

This talk will demonstrate how to use Object-Oriented programming patterns, specifically polymorphism, to handle conditional logic resulting in code that is easy to modify. The material will be presented in the context of a real-world code refactor for an open-source project. We will walk through the initial solution and discuss its limitations before diving deep into the refactored codebase.

This talk is geared towards developers who do not have a lot of experience implementing Object-Oriented solutions. After this talk, you will be able to identify situations where Object-Oriented design can be used to simplify complex conditional logic. Following the steps outlined, you will be able to refactor the design without changing existing functionality.

### Outline

- Introduction to topic and to speaker (2 minutes)
- Code Smell (3 minutes)
  - What's a code smell?
  - What do code smells indicate?
- Case Study: Chicago Python Slack bot (5 minutes)
  - High-level intro to community engagement tool
  - Discussion of GitHub Summary feature
  - Initial solution -- hackathon
  - Try to make a change, seems painful
- Object-Oriented Programming (OOP) (8 minutes)
  - High-level intro
  - OOP in Python
  - What is polymorphism?
  - Polymorphism in python
- Case Study Revisited: After Code Refactor (8 minutes)
  - Break problem down -- what are we trying to do
  - Walk thru new solution
  - Walk thru code
  - Show how we can extend for a new case
- Closing (6 minutes)
  - Benefits of if statements -- it's about tradeoffs
  - Generalize steps to refactor if statements into polymorphic classes
  - Shoutout to testing

## Notes

I have given a shorter version of this talk at a local Python meetup. The audience appreciated the use of a case study to help solidify abstract Objected-Oriented concepts with real-world code examples.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed here: youtube.com/playlist?list=PLi5-nQFgraTq0WTtjQc7OY7ywpBA86e7i

## Slides link (optional)

[http://bit.ly/code-smell-if-statements](http://bit.ly/code-smell-if-statements)
