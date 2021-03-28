# Testing with Real Fake Data

# Real World Testing Tutorial

## Todo

- [x] read `factoryboy` docs
- [x] learn how to use Faker effectively
- [x] combining them together
- [ ] create custom faker provider
- [ ] Tips on getting Factory boy into sql alchemy session

## Length

30

## Audience Level

Intermediate

## Elevator Pitch

It's hard to write a good test case - the act requires just enough thinking that it makes testing harder than it should be.



The hardest part of testing is coming up with test cases for each of our tests


The hardest part of testing is setting up your test environment to a known state so we can have reproducible tests.

A test case has 3 stages: setup test environment, perform action, and validate action was performed.


Setting up the test environment takes up most of the time when writing tests.

The hardest part of this process is setting up a test environment. Creating realistic test data is hard so we end up using the same test fixture for many different tests.

Each test case has 3 phases: Arrange test environment, perform Action, Assert conditions.

asdfasf

Writing tests with real data can ensure our program works as expeted. Generating good test data is hard so we end up using the same test fixture for many different tests.  our tests start to depend on each other and things become hard to understand.

The boundaries between tests begin to blur. Soon tests depend on each other. This talk will demostrate how we can use fixture factories to create an environment that models a real world situation.



Tools like `Faker` and `factory_boy` generate complex test objects we can use to model real world scenarios.

Level up your testing with fixture factories.

We spend the majority of time writing tests is to spent setting up the test environment to a known state. When tests

Setting up each test case to a known state is the primary activity

We spend the majority of time writing tests is to spent setting up the test environment to a known state. When tests get more complex and as the relationships between objects grow, test fixtures become



When writing tests

This

We spend the majority of each of our tests setting up the environment to the exact

In this talk we will explore how we can use `Faker` and `factory_boy` to generate compelx test objects that model

In this talk use `Faker` and `factory_boy` to create test objects we can use

Tired of manually writing test data?

 In this talk we will explore two Python libraries that make it easy for us to create complex test objects we .


Manually generating complex test objects which model real-world situations by hand makes test code hard to understand.

Since we are spending the majority of time

## Description

Test fixtures are a [].

A test consists of 3 stages: setting up an environment, performing an action, and validating the result. Most of our testing time is spent getting the environment into a known state. This is known

Test fixtures are often reused across unrelated tests which makes fixtures bloated and increases the runtime of the test suite.

People reuse test fixtures across many different types of tests. The fixtures can be bloated and add to the runtime of tests that don't require them.

Helper functions help us create test fixtures, but now we have code

The majority of time spent writing tests is getting our environment into a known statement.



Tools like `factory_boy` and `Faker` enable us to create complex test fixtures with only a few lines of code.

Test fixtures are used to setup

Tests help us ensure that our system worked as intended

Generating test data is often a manual process which means we are either creating test helpers

testing folks getting better

### Outline

factory boy and faker
create a custom provider
https://hacksoft.blog/improve-your-tests-django-fakes-and-factories/
mockeroo.com

- brief overview of tests
  - why are tests important
  - types of tests
  - most tests require us to se
- test fixture
- Arrange-Act-Assert

## Notes

This will be my first time giving this talk at a conference. If selected, I will be previewing this talk at a Chicago Python event i

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyCon Balkan, PyTennessee, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

## Slides link (optional)

[http://bit.ly/code-smell-if-statements](http://bit.ly/code-smell-if-statements)

## Resources

https://www.rover.com/blog/engineering/post/speeding-django-test-runs-optimizing-factory-boy/

alternatives: https://github.com/model-bakers/model_bakery

https://hacksoft.blog/improve-your-tests-django-fakes-and-factories/

mockaroo
