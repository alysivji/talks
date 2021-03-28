# Everyday Design Patterns: Observer Pattern

## Todo

- [ ] write blog post talking about how awesome it is in JS
  - Python implementation from scratch; reference pyee
- use pyee in busy beaver
  - [ ] blog post about how PyEE will make asyncio useable
  - use with FastAPI

## Resources

- https://www.one-tab.com/page/BxAfNa_3Q2qKpi_bRb0gzw

## Notes

- Slack webhook trying to do something when an event happens
- first attempt is a bunch of if statements that check for a certain type of event and then do an action
  - this is okay, but is starts to become unmanageble
  - testing is fine at first, but it gets harder
- move each block in conditional to function
  - testing is easy
  - we still have a giant if block that we have to test
- dispatch events when we get them aka emit events when we get them
  - dictionary dispatch. why, not wrap this in a class?
  - draw the early stages of the event emitter
    - in node there is an `EventEmitter` object
    - the more i drew out what i had, it started to look like it

- in the real world... if this loosk familiar
  - flask does this
  - django signals use the observer pattern
  - what else uses the observer pattern?
    - DOM, UIs, PPB?

- design patterns used properly feel like they fit and make everything work together
  - feels natural
  - improves API
  - using the eventemitter felt natural that I wanted to use it again and isnt that the whole point of design patterns
  - they are tried and tested solutions to commonly occuring problems in software design

- pyee
  - how to use classes
  - this is good because it can plug into event loops
    - asyncio, twisted

- formal definition
  - Pub/Sub
  - honestly even after learning it, i didn't see it until it all clicked
  - don't have to implement design patterns exactly how they are stated
    - the point is to adapt them to fit your code
    - it's the high-level concepts that help us communicate versus doing things exactly the way it's stated in literature

- takeaway: if you like somethng about a library, find out why you like it
  - digging deeper and learning about these patterns will improve your design
