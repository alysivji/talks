# If Statements are a Code Smell

## Length

30

## Description

Writing software is about making trade-offs between getting things done and doing them right. Time constraints often force us to take shortcuts to handle slight variations resulting in patches of conditional logic sprinkled throughout our codebase. Workarounds that once allowed us to move quickly now hinder our progress in getting new features out to customers. It doesn't have to be this way!

This talk will demonstrate how to use Object-Oriented programming patterns, specifically polymorphism, to handle conditional logic resulting in code that is easy to modify. The material will be presented in the context of a real-world code refactor for an open-source project. We will examine the initial solution, discuss its limitations, and walk through the process of refactoring nested `if` blocks into polymorphic classes.

### Outline

- Introduction to topic and to speaker
- If statement
    - Overview with examples
    - Hard-to-read code
    - MIGHT be something we need to look into
- Compound If
    - Discuss limitations + how to refactor
- Nested If
    - Discuss limitations + how to refactor
-  Case Study (Duplicate If)
    - Overview with introduction to problem
    - Initial solution (hackathon)
    - Try to add a new feature, it's difficult
    - Discuss limitations
- Object-Oriented Programming
    - High-level intro
    - Dive into polymorphism with detailed example
- Case Study Revisited (Duplicate If)
    - Break the problem down -- what are we trying to do
    - Walk thru refactor process
    - Add new feature with ease
- Closing
    - Benefits of if statements -- it's about tradeoffs
    - Explicitly define steps to refactor if statements into polymorphic classes
    - Shoutout to testing
    - Shoutout to learning by developing open-source software

## Audience Take-Aways

After this talk, you will be able to identify situations where Object-Oriented design can be used to simplify complex conditional logic. Using the steps outlined, you will be able to refactor code to improve software architecture without changing existing functionality.
