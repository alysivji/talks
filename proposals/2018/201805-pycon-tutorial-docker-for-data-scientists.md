# PyCon Tutorial Proposal

(based on [PyCon Tutorial submission form](https://us.pycon.org/2018/proposals/submit/tutorial/))

[Detailed Tutorial Information](https://us.pycon.org/2018/speaking/tutorials/)

## Title

Docker for Data Science

## Description

> Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs.

Jupyter notebooks simplify the process of developing and sharing Data Science projects across groups and organizations. However, when we want to deploy our work into production, we need to extract the model from the notebook and package it up with the required artifacts (data, dependencies, configurations, etc) to ensure it works in other environments. Containerization technologies such as Docker can be used to streamline this workflow.

This hands-on tutorial presents Docker in the context of Reproducible Data Science - from idea to application deployment. You will get a thorough introduction to the world of containers; learn how to incorporate Docker into various Data Science projects; and walk through the process of building a Machine Learning model in Jupyter and deploying it as a containerized Flask REST API.

## Audience

> 1–2 paragraphs that should answer three questions: (1) Who is this tutorial for? (2) What background knowledge or experience do you expect students to have? (3) What do you expect students to learn, or to be able to do after attending your tutorial?

This session is geared towards Data Scientists who are interested in learning about Docker and want to understand how to incorporate it in their projects. No prior knowledge of Docker is assumed. Proficiency with Git and the Command Line is not a prerequisite, but will make it easier to follow along.

Upon completion of this tutorial, students will be able to:

* Navigate the Docker ecosystem with ease
* Leverage containers as part of their data science workflow
* Productize & deploy a Machine Learning model wrapped in an API

Learn how to become a Full-Stack Data Scientist!

## Outline

> Make an outline that lists the topics and activities you will guide your students through over the 3 hours of your tutorial. Provide timings for each activity — indicate when and for how long you will lecture, and when and for how long students will be tackling hands-on exercises. This is a very important criteria! Generally speaking, the more detailed the outline, the more confidence the committee will have that you can deliver the material in the allotted time.

1. Course and Instructor Introduction (3 minutes)
    * Make sure everybody is in the right location
    * Instructor Bios
    * High level overview of next three hours

1. Go over system requirements and where to find course materials (2 minutes; total time: 5 minutes)
    * Students will need a working laptop with a WiFi connection
    * Students will need to be running one of the following Operating Systems:
        * Windows
        * Mac
        * Linux
    * Required software:
        * Git command line tools
        * Docker
        * Docker Compose
    * Link to course material on Github
        * Have students pre-download a few Docker images to reduce strain on the conference WiFi
    * Unprepared students will have time to get their system set up during the first set of lecture

1. Reproducible Data Science - Lecture (5 minutes; total time: 10 minutes)
    * Overview of Data Science
    * Need for Full-Stack Reproducible Data Science
    * Discuss how Docker solves the problem of reproducibility
    * Note: this section will be adapted from the [Data Science Workflows using Docker Containers](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/) presentation

1. Introduction to Docker - Lecture (15 minutes; total time: 25 minutes)
    * High level overview of Docker
    * Containers vs Virtual Machines
    * Applications of Docker
    * Docker Architecture
    * DockerHub
    * Docker Objects (images / containers)
    * Creating images: `docker commit` vs Dockerfile
    * Overview of useful Docker commands
        * Provide cheatsheet handouts (also on Github)
    * Best Practices + Tips & Tricks
    * Note: this section will be adapted from the [Data Science Workflows using Docker Containers](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/) presentation

1. Introduction to Docker - Hands-on Lab (20 minutes; total time: 45 minutes)
    * Pull image from Docker Hub
        * Small image (we got you conference WiFi)
    * Start a container
    * Stop a container
    * Shell into container
    * Kill container
    * Delete container
    * Hello World Dockerfile
        * Students will create from scratch
    * Delete image

1. Data Science Workflows with Docker Containers - Lecture / Demonstration (15 minutes; total time: 1 hour)
    * Walking through actual applications of Docker
        * Workflow #1: Self-Contained Container
        * Workflow #2: Data Science Project
        * Workflow #3: Data Driven Application
        * Workflow #4: Data Science API
    * Note: this section will be adapted from the [Data Science Workflows using Docker Containers](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/) presentation

1. Data Science Workflow - Hands-on Lab (20 minutes; total time: 1 hour and 20 min)
    * For two of the workflows from the previous section, students will:
        * Write a Dockerfile from scratch following requirements and directions from previous section
        * `docker build` to create an image
        * `docker run` to initialize container
        * Run process inside container to confirm everything works
    * There will be exercises for all four workflows if students finish before the allocated time or want to work over the break
        * Solutions will be provided

1. Break (15 minutes; total time: 1 hour 35 min)

1. Introduction to Project and related Topics - Lecture (10 minutes; total time: 1 hour 45 min)
    * Project Description
        * Note: We are thinking of building out a classification model in Jupyter, pickling it and wrapping it with a REST API inside of a container (using Flask RESTful). We will plug this container into our web application that is powered by Docker Compose. This web application will have a front end which allows users to upload CSV files; app will create predictions based on input and store data inside of a Postgres database container. This project is subject to change.
    * Overview of `pickle` and the benefits of serialization
    * What is REST and how can we interact with APIs?

1. Building and pickling ML model - Hands-on Lab (5 minutes; total time: 1 hour 50 min)
    * We will provide a Jupyter notebook containing a pre-built model with a few empty cells for Exercises
    * Students will:
        * Save tuned model to disk
        * Load pickled model from disk
        * Make predictions using model and given inputs
    * This notebook serves as the basis for the Flask container

1. Build REST API Container - Lecture / Demonstration (10 minutes; total time: 2 hours)
    * Walk through the process of extracting the required code from Jupyter and putting it the provided Flask RESTful template
    * Fill in template Dockerfile
    * Build image and launching container
    * Testing endpoint works with  `requests.get()`

1. Build REST API Container - Hands-on Lab (10 minutes; total time: 2 hours 10 min)

1. Docker Compose Overview - Lecture (20 minutes; total time: 2 hours 30 min)
    * In context of multi-container Data Science applications.
    * Introduce Docker Compose and provide a high-level overview of its core concepts and operation.
    * Overall Goals of Compose Integration:
        * Create a simple, dynamic interface for Data Scientists to download and easily run a fully-working copy of a Data Science Application.
        * Bundle all internal and external package and code dependencies into a single buildable configuration.
    * Indicate use-cases where it would and would not be appropriate.
    * Make parallels between Docker and Docker Compose.
        * Show the equivalent Docker and Docker Compose commands.
        * Show what to put in a Compose file vs what to put in a Dockerfile.
        * Walk through a Compose file.
        * Introduce concepts such as services, ports, volumes, networks, environment variables, and much more.
        * Work through common issues with Compose.
    * Demonstrate how to execute a Docker Compose file.

1. Build and Launch Data Application - Lecture / Demonstration (10 minutes; 2 hours 40 minutes)
    * Begin integrating previous project into a Docker Compose-based workflow.
        * Introduce Docker images needed for this project
            * Dockerfile-based image, Nginx, and Postgres
        * Introduce project boilerplate with barebones Compose file needed for lab
            * Compose will facilitate creating a web-interface for exposing data to end-users.
        * See Project Description section below
    * Show strategies for working through common Docker development issues.

1. Hands on Project (15 minutes; total time: 2 hours 55 min)
    * We will provide all the building blocks that go into this data driven application (i.e. other containers)
    * Students will plug their container from the previous exercise into the given template
    * Modify the Docker Compose file and `docker-compose up` to get the application running
    * Verify it works

1. Summary and Next Steps (5 minutes; total time: 3 hours)
    * Where to go from here

## Additional Notes

> (a) If you have offered this tutorial before, please provide links to the material and video, if possible. Otherwise, please provide links to one (or two!) previous presentations by each speaker. (b) Please summarize your teaching or public speaking experience and your experience with the subject of the tutorial. (c) Let us know if you have specific needs or special requests — for example, requests that involve accessibility, audio, or restrictions on when your talk can be scheduled.

### Joe Jasinski Background

Joe has been working with Python and Django since 2008, and leads the Technology Department at Imaginary Landscape, a Chicago-based Python web-development firm. He's given numerous talks at ChiPy, DjangoCon, and other venues on Python-related topics, and he is a co-organizer of the Chicago-based Python user group, ChiPy. He is a mentor in the ChiPy mentorship program, and frequently trains developers at work. Joe loves working with Docker, and has been using it for a number of years with the goal of creating the ideal Docker Deployment/Development environment. In his free time, he's been working on building a Raspberry Pi Kubernetes cluster.

List of talks:
[https://www.joejasinski.com/video/](https://www.joejasinski.com/video/)

Docker blog posts:
 - [Docker: Develop with Private Git Repositories in requirements.txt file](http://www.djangocurrent.com/2017/10/docker-develop-with-private-git.html)
 - [Django Docker and Celery](http://www.djangocurrent.com/2017/06/django-docker-and-celery.html)

### Aly Sivji Background

Aly is a Mathematician / Software Engineer at Analyte Health and a part-time grad student at Northwestern University studying Medical Informatics. He has presented his Docker talk, [_Data Science Workflows using Docker Containers_](https://github.com/alysivji/talks/tree/master/data-science-workflows-using-docker-containers), at PyOhio, Denver Data Science Day, and various meetups around Chicago.

List of talks:
[https://github.com/alysivji/talks](https://github.com/alysivji/talks)

Selected videos:

* [Data Science Workflows using Docker Containers](https://www.youtube.com/watch?v=oO8n3y23b6M)
    * [Slides](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/)
* [A Gentle Introduction to Context Managers](https://www.youtube.com/watch?v=hy-O0Qpr_Us)

### Tathagata Dasgupta Background

Tathagata (T) is a Senior Engineer working on Highly Automated Driving at Here Technologies, Chicago. As an organizer of the Chicago Python (ChiPy) user group, he started the ChiPy Mentorship program in 2014, a free and volunteer run event, which has helped over a hundred developer advance their programming skills. He is also the lead organizer of the monthly-held Chicago Python Project Night and loves coming up with hands-on exercises to teach hungry minds Python, web development and data science.

* [Talk on the ChiPy Mentorship program](https://www.youtube.com/watch?v=l9xwgde6J84)

Comments from Satisfied Python Project Night "Customers":
> People in my team challenge group learned a lot of useful pandas and Jupyter tricks. Another spot-on level of difficulty for both beginners and more advanced users who wanted to take it to the next level. - [*Zax R*](https://www.meetup.com/_ChiPy_/events/xshqwmywpbvb/)
>
> It was a very productive and educational meetup. I learn a lot at these events. - [*Mark W*](https://www.meetup.com/_ChiPy_/events/239174122/)
>
> It was very good. It is great to experience all of the energy in the group and I learn a lot. - [*Joe K*](https://www.meetup.com/_ChiPy_/events/239174122/)
