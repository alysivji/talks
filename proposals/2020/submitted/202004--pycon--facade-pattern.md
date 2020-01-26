# Everyday Design Patterns: Facade Pattern

## Length

30

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

Developers spend lots of time writing code to integrate third-party packages and APIs into our project. Directly adding dependencies into business logic couples our code to something we do not control. This makes code hard to modify and even harder to test. When upstream packages change, we spend additional time updating integration code across the codebase.

This talk demonstrates HOWTO use object-oriented programming principles, specifically abstraction and encapsulation, to hide complexity and isolate the impact of changes. By using an API version upgrade as our guiding example: we will walk through the initial implementation, discuss its limitations, and show how the Facade Pattern improves software design.

After this talk, you will be able to use the Facade pattern to write robust code that is easy to maintain.

## Who and Why (Audience)

> 1–2 paragraphs that should answer three questions: (1) Who is this talk for? (2) What background knowledge or experience do you expect the audience to have? (3) What do you expect the audience to learn or do after watching the talk

The session is geared towards developers of all levels looking for a friendlier approach to Design Patterns. By applying the principles outlined, you will be able to use the Facade pattern to write robust code that is easy to maintain.

### Outline

> The “outline” is a skeleton of your talk that is as detailed as possible, including rough timings or estimates for different sections. If requesting a 45 minute slot, please describe what content would appear in the 45 minute version but not a 30 minute version, either within the outline or in a paragraph at the end.

- Introduction to topic and speaker (2 minutes)
- Design Patterns Introduction (3 minutes)
    - What are design patterns?
    - Benefits of patterns
    - Types of Patterns: Creational, Structural, Behavioral
- Case Study: Interacting with APIs (6 minutes)
    - Introduce problem -- downloading data from 3rd party API
    - Walk thru initial solution (direct integration)
    - API changes...!!! Changing our code is painful!
    - Aside: tests are complicated to write
- Object-Oriented Programming (OOP) (6 minutes)
    - High-level intro
    - Principles of OOP
    - Dive into encapsulation and abstraction
    - Encapsulation and abstraction in Python
- Case Study Revisited: Facade Pattern (10 minutes)
    - Adding a layer between the API and implementation enables changes to be isolated
    - Walk through the process of changing code to support new API
    - Show how facade pattern simplifies testing with fakes
    - Other examples of Facade pattern in practice: wrap Python libraries
- Closing (3 minutes)
    - Benefits of Design Patterns
    - Program to an interface, not an implementation
    - Don't get too hung up on diagrams and terminology
    - Focus on understanding the problem you are trying to solve

## Additional Notes

> Anything else you would like to share with the committee:
> Speaker public speaking experience.
> Speaker subject matter experience.
> Have the speaker(s) given this presentation before elsewhere?
> Links to recordings, slides, blog posts, code, or other material.
> Specific needs or special requests — accessibility, audio (will you need to play pre-recorded sound?), or restrictions on when your talk can be scheduled.

I will be presenting this talk at PyTennessee in March 2020. I have previously given a lightning talk about the Facade Pattern at a Chicago Python meetup.

I have experience in breaking down complex concepts into easily understood components. I recently gave a talk on how if statements can be refactored into polymorphism classes at PyCon Balkan. The audience appreciated the use of a real-world code example to help solidify abstract object-oriented concepts.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyOhio, PyTexas, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist
