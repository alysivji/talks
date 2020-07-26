# Object-Oriented Python with `functools.partial`

This folder contains notes for my talk.

## Slides

### Example Class

```python
class Developer:
    def __init__(self, github_id, favourite_language):
        self.github_id = github_id
        self.favourite_language = favourite_language

    def eat(self):
        pass

    def sleep(self):
        pass

    def work(self, coffee):
        return "code"
```

### Initiailizing Class

```console
>>> aly = Developer(github_id="alysivji", favourite_language="Python")
>>> aly.github_id
'alysivji'
>>> aly.favourite_language
'Python'
>>> type(me)
<class 'Developer'>
```

### Sorting Example

```python
from collections import namedtuple

Movie = namedtuple("Movie", "title release_year")

movies = [
  Movie(title="Furious 7", release_year=2015),
  Movie(title="The Fast and the Furious: Tokyo Drift", release_year=2006),
  Movie(title="2 Fast 2 Furious", release_year=2003),
  Movie(title="Fast & Furious", release_year=2009),
  Movie(title="F9", release_year=2021),
  Movie(title="Fast & Furious 6", release_year=2013),
  Movie(title="The F8 of the Furious", release_year=2017),
  Movie(title="Fast Five", release_year=2011),
  Movie(title="The Fast and the Furious", release_year=2001),
]

# do star wars (first 9)

sorted(movies)
sorted(movies, key=lambda movie: movie.release_year)
```
