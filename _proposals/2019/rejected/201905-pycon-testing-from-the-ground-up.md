# Testing from the Ground Up

## Length

45

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

Tests ensure our program works as intended and that changes to the codebase do not break existing functionality. However, these benefits are not free; we need to have a plan to write our application and a plan to test it.

Seasoned developers can balance writing code to solve business problems with writing tests to ensure correctness and prevent regression. Finding this balance and knowing what to test can feel more like an art than a science, especially to those new to the industry. This talk will introduce concepts and techniques that can be used to write effective tests by exploring the following topics:

* Benefits of testing
* Blackbox vs whitebox testing
* Automated vs manual testing
* Types of tests
* Test metrics
* Tools that simplify the testing process

## Who and Why (Audience)

> 1–2 paragraphs that should answer three questions: (1) Who is this talk for? (2) What background knowledge or experience do you expect the audience to have? (3) What do you expect the audience to learn or do after watching the talk?

This session is geared towards developers who want to write tests but are not sure where to start. After this talk, test newbies will have all the skills and knowledge to write their first test. Attendees with testing experience will be exposed to tools and techniques that can make them more effective testers.

## Outline

> The “outline” is a skeleton of your talk that is as detailed as possible, including rough timings or estimates for different sections. If requesting a 45 minute slot, please describe what content would appear in the 45 minute version but not a 30 minute version, either within the outline or in a paragraph at the end.

1) Introduction + my testing journey (3 minutes)

> Start to emphasize the theme of the talk. Tests give us confidence in our code: confidence that our code is producing expected results and confidence that we can make changes without breaking existing functionality.

2) A walkthrough of an example application that will demonstrate testing concepts (5 minutes; total time: 8 minutes)

> Created a no-frills application that will be used to demonstrate various testing concepts. Walk through the architecture of the app and start thinking about ways we can test.

3) Deep dive into testing (12 minutes; total time: 20 minutes)

> Plan to go over definitions, black box vs white box testing, automated vs manual testing, an overview of the testing pyramid with examples in the context of the above application, and a discussion of the benefits that testing provides.
>
> I'll provide a brief intro to test metrics with a sidebar on how metrics can be gamed (i.e. measurement changes behavior)

4) Test Frameworks (10 minutes; total time: 30 minutes)

> Discussion of tools that make testing easier, `unittest` vs `pytest`, and why `pytest` wins.
>
> Dig into pytest features: how to define assertions, detailed introspection of test failures, fixture model, fixture factory pattern, pytest markers, parameterized tests, and intro to plugin model.
>
> Run pytest on example app and show how we can use `pdb` to step into broken tests to introspect objects at runtime.

5) Testing tools (10 minutes; total time: 40 minutes)

> A survey of the landscape of tools that can ease the pain of testing. Look at useful pytest plugins, test double libraries, alternatives to test doubles for HTTP requests, tools for browser / API testing, and survey of other software that can be used for testing purposes.
>
> Depending on the time slot available, this will be either a high-level overview with a short description of each tool that I can combine with the previous section. With additional time, I can present examples of how tools can be used in different scenarios.

6) What to test and how to write good tests (5 minutes; total time: 45 minutes)

> This section will be included if I have the longer timeslot. Will discuss what to test (functional requirements, basis path testing, equivalence partitioning, boundary analysis, classes of bad data, data flow testing, error guessing) and how to write good test (Arrange-Act-Assert / Given-When-Then).

## Additional notes

> Anything else you would like to share with the committee:
> Speaker public speaking experience.
> Speaker subject matter experience.
> Have the speaker(s) given this presentation before elsewhere?
> Links to recordings, slides, blog posts, code, or other material.
> Specific needs or special requests — accessibility, audio (will you need to play pre-recorded sound?), or restrictions on when your talk can be scheduled.

At my last job, I was responsible for building out an integrated testing framework for a microservices-based backend architecture. This project required me to dig into testing tools and techniques which increased my team's testing efficiency and enabled us to ship code faster. Since then I have been organizing my thoughts into a [blog series](https://alysivji.github.io/drafts/testing-101-introduction-to-testing.html) and talk in order to create the resource I that would have wanted when I first got started testing. These resources have been incorporated into team activities at Chicago Python Project Night.

I previously presented this talk at a couple of local Python meetups (IndyPy, Chicago Python). Beginners appreciated how I did not make assumptions about previous knowledge and folks with testing experience told me they learned new tools and techniques they could add to their arsenal.

[Link to Slides](https://docs.google.com/presentation/d/1oI29-S6wFs8Yeqe5TouFak2kPF-pqnvNd66yQWn12Vs/edit?usp=sharing).

---

## Bio

Aly Sivji is a Canadian expat living in Chicago. By day, he builds containerized data pipelines at Nielsen. By night, he is a co-organizer of the Chicago Python Users Group (ChiPy). Aly is an active participant in ChiPy’s Mentorship Program and loves helping intermediate developers get over the hump to become experts. Outside of Python, Aly enjoys cycling, reading, and rewatching old TV shows.
