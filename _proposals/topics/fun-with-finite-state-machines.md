# Fun with Finite State Machines

## Length

15-20 (in its current state)

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

Finite State Machines (FSM) are tools we can use to model simple and complex workflows. In this (non-mathematical) talk, we will learn about FSMs and examine how they can be used to improve software design. We’ll finish by diving deep into a couple of Python implementations of FSMs.

Full disclosure: one of the implementations is a library I created.

## Additional Things to Cover (in longer version)

- working through how to implement a finite state machine workflow for a problem you are given

- Add a new state (DRAFT) and see how that changes things
- when to use state machines
  - Adding a state or status field to your model is the most obvious sign of a state machine.
  - Boolean fields are usually also a good indication, like published, or paid. Also timestamps that can have a NULL value like published_at and paid_at are a usable sign.
  - Finally, having records that are only valid for a given period in time, like subscriptions with a start and end date.
- How to implement State Machines?
  - Think of states
  - Think of transitions
  - Code and test
- Why are state machines useful?
  - Come back to this at the end
  - Help in designing explicit workflows
  - Clearer code that describes process
  - Reduce if statements (which I don’t know if anybody has heard… are a code smell)
  - Add audit log (you will have to build tooling around capturing state changes | OR YOU CAN USE django-fsm and django-fsm-log)
