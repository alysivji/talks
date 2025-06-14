# Orchestrate Data Pipelines with Django, Celery, and Finite State Machines

## Session Type

45-minute-talks

## Track

General

## Abstract

Building and executing data pipelines doesn't require specialized orchestration software. This talk demonstrates how Django, Celery, and the django-fsm library can be used to write scalable, efficient, and fault-tolerant data pipelines.

## Description

Building and executing data pipelines doesn't require specialized orchestration software. This talk demonstrates how Django, Celery, and the django-fsm library can be used to write scalable, efficient, and fault-tolerant data pipelines.

In the context of a building a health data ingestion framework, we will explore the use of: Django to view and manage pipelines; Celery for task management and asynchronous processing; and django-fsm for implementing Finite State Machines to control the pipeline and handle errors.

Attendees will gain practical knowledge and learn best practices, empowering them to create efficient, resilient, and maintainable data pipelines with tools from the Django ecosystem.

## Notes

This will be my first time giving this talk. I came up with the idea for this talk after evaulating Airflow, Prefect, and Dagster and realizing it would be cheaper and faster to leverage the Django ecosystem to build our health data ingestion framework.

If this talk gets selected, I will be talking to my CTO about open sourcing a Django management command that automatically generates [Mermaid Markdown state diagrams](https://mermaid.js.org/syntax/stateDiagram.html) from Django models that use the django-fsm library. This tool has been helpful in visually documenting data pipelines.

On top of being a regular speaker in the Chicago tech community, I have also spoken at PyCon Africa, EuroPython, and led a 3-hour tutorial at PyCon US. A selection of previous talks can be viewed at https://bit.ly/siv-talks-playlist

## Profile

Aly Sivji is a Canadian ex-pat living in Chicago. By day, he works as a Team Lead at Jasper Health building a digital health platform to improve the management and delivery of cancer care. By night, he co-organizes the Chicago Python Users Group (ChiPy). Aly is an active participant in the ChiPy Mentorship Program and he loves helping intermediate developers become experts. Outside of Python, Aly enjoys cycling, reading, and rewatching old TV shows.

## Notes

- airflow, prefect, dagster
  - dags
  - what is a dag?
  - how is a dag like a state machine?
  - we won't be able to spin up complex tasks -- to run multiple concurrent workers for a single task, but how many times do you really need to do that?
- retry logic, observability?
- use celery cron to schedule
- open source django fsm tool
- adding more workers if you are on kubernetes
