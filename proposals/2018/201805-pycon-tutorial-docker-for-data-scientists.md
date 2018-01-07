# PyCon Tutorial Proposal

(based on [PyCon Tutorial submission form](https://us.pycon.org/2018/proposals/submit/tutorial/))

[Detailed Tutorial Information](https://us.pycon.org/2018/speaking/tutorials/)

## Title

Docker for the (Full-Stack) Data Scientist

```python
# title should be simple like Docker for Data Scientists or Docker for Data Science
# maybe have "become a full stack data scientist" in the audience description
```

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

## Audience

>  1–2 paragraphs that should answer three questions: (1) Who is this tutorial for? (2) What background knowledge or experience do you expect students to have? (3) What do you expect students to learn, or to be able to do after attending your tutorial?

## Outline

> Make an outline that lists the topics and activities you will guide your students through over the 3 hours of your tutorial. Provide timings for each activity — indicate when and for how long you will lecture, and when and for how long students will be tackling hands-on exercises. This is a very important criteria! Generally speaking, the more detailed the outline, the more confidence the committee will have that you can deliver the material in the allotted time.

## Additional Notes

> (a) If you have offered this tutorial before, please provide links to the material and video, if possible. Otherwise, please provide links to one (or two!) previous presentations by each speaker. (b) Please summarize your teaching or public speaking experience and your experience with the subject of the tutorial. (c) Let us know if you have specific needs or special requests — for example, requests that involve accessibility, audio, or restrictions on when your talk can be scheduled.

---

*my submission for PyTennessee*

## Brief Description

Jupyter notebooks make it easy to create reproducible workflows that can be distributed across groups and organizations. This is a simple process provided our end-users have access to the data along with a compatible Python environment. Learn how to use Docker to package a shareable image containing the libraries, code, and data required to reproduce every calculation.

## Detailed Abstract

Containerization technologies such as Docker enable software to run across various computing environments. Data Science requires auditable workflows where we can easily share and reproduce results. Docker is a useful tool that we can use to package libraries, code, and data into a single image.

This talk will cover the basics of Docker; discuss how containers fit into various Data Science workflows; and provide a quick-start guide that can be used as a template to create a shareable Docker image!

Learn how to leverage the power of Docker without having to worry about the underlying details of the technology. Although this session is geared towards data scientists, the underlying concepts have many use cases (come find me after to discuss).

## Additional Notes

* [Link to slides](http://bit.ly/docker-for-data-science)
* [Previous talks](https://github.com/alysivji/talks)

For this talk, I assume no knowledge of Docker. We will build up from first principles and I alternate between slides and the terminal to guide the audience thru my workflow and thought process.

---

## Thoughts for Tutorial

Right now the basic idea is to take my talk and make it into lab exercises. Explain a concept and then let people go off and type in commands to learn.

Simple outline for exercises
* pulling an image and getting a container running
* shelling into a container and changing something
  * can build exercises around this fairly easily
* freezing changed container into an image we can use to build more containers
* creating a basic hello world docker image via dockerfile
* uploading said image to dockerhub

* other misc docker things like docker kill, docker start, maybe something about docker networking (this is a huge topic by itself, so maybe nothing about networking)

* going into a lot more depth about data science workflows
  * for each of the workflows from my talk, making it into a lab exercise where attendees would have to create a dockerfile, make an image, and then start a container
  * 4 workflows * 15 minutes = 1 hour is more or less already planned out

We use Docker at work so maybe have an aside on how to develop inside of containers as I learn more.

There is also Pachyderm which is a pretty cool project. Can use to build containerized machine learning pipelines. I haven't used it before, but the docs are good and it seems easy enough to set up a basic data science pipeline as an advanced exercise
http://pachyderm.readthedocs.io/en/latest/getting_started/beginner_tutorial.html

My talk is around 40 minutes so most of the material is ready to go. Just about putting it together in a format that can be easy to understand. I did watch a few Docker tutorials from PyCon as I wrote this up back in July. Will definitely review as I'm writing this up.

Also, no problem about not knowing Docker. There is a pluralsight course called Docker deep dive that taught me everything I know. You can use my account to watch.

No worries if you can't do it. Time is a limited resource and you gotta make sure you are spending it doing the best thing for you.
