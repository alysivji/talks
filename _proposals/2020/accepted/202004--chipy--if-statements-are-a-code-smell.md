# If Statements are a Code Smell

## Length

30

## Audience Experience Level

Novice

## Description

`if` statements are elements of a programming language that allow us to control what statements are executed. By chaining together a series of `if` statements, we can solve any problem we can think of. But code with too many `if` statements is hard to read and even harder to change. Workarounds that once allowed us to move fast, now get in the way when we go in to make modifications. It doesn’t have to be this way!

This talk demonstrates HOWTO handle complex conditional logic with simple Python classes. The material will be presented in the context of a code refactor for an open-source project: we examine the initial solution featuring duplicate `if` statements, show how hard it is to make a change, and walk through the process of refactoring `if` blocks into polymorphic classes. The case study has been simplified to illustrate concepts you can apply to your own code.

After this talk, you will be able to identify situations where an object-oriented solution can be used to improve software design. You will also be exposed to tradeoffs we need to think about before refactoring to higher-level abstractions.

## Private Submission Notes

n/a

## Slides link (optional)

[http://bit.ly/code-smell-if-statements](http://bit.ly/code-smell-if-statements)
