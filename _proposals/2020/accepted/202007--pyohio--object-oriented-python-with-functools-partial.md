# Object-Oriented Python with `functools.partial`

## Submission Type

- Thunder Talk (10 minutes)

## Description

> Please enter a short description of the talk to be used on the schedule and talk detail pages of the PyOhio website. This content will be shown publicly.

In Python, **everything** is an object -- `int`s, `bool`s, `class`es, and, yes even `function`s. This has many benefits, but it also allows us to write un-Pythonic code that is hard to follow.

This talk will demonstrate HOWTO design Object-Oriented solutions using only functions, built-in data structures, and the standard library.

After this talk, attendees will have a better understanding of how Python classes `function` behind the scenes.

### Outline

- Everything is an object
- What makes a `class` a `class`
- Introduce case study: chess
    - short overview of chess for context
    - implement `Piece` with just a function
- Faking inheritence with `functools.partial`
    - create pieces and initialize board
- Attribute access with `types.SimpleNamespace`
    - if you squint, code looks Object-Oriented
- Faking behavior with inner functions
    - piece movement logic requires an inner function
    - overview of scope, closures, inner functions
    - how it applies to chess
- Conclusion
    - do not attempt this in production
    - use class to store state and perform actions
    - classes are nice, we should use them (when necessary)

## Notes

> These notes are meant for the organizers and won't be made public.

I spent a couple of hours playing around with this concept. Implemented the beginnings of a chess game with just functions. Have a path forward in getting enough done to demonstrate my point.

The outline might seem like I'm going to be covering a lot, but this talk will be going over concepts at a high-level with links to dig into later. An example slide deck for a previous thunder talk (75 slides in ~8 minutes) is available at: http://bit.ly/life-without-pip

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyTexas, PyTennessee, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

If this talk is selected, could you please remove the outline from the description that gets posted to the website? Thank you!

## Talk Objective

> What is your desired takeaway for the audience?

The audience will have a better understanding of how Python classes work under the hood.

## Bio

Aly Sivji is a Canadian expat living in Chicago. By day, he builds backend systems at Numerator. By night, he is a co-organizer of the Chicago Python Users Group (ChiPy). Aly is an active participant in the ChiPy Mentorship Program and he loves helping intermediate developers become experts. Outside of Python, Aly enjoys cycling, reading, and rewatching old TV shows.
