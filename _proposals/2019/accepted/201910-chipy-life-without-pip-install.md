# Life without `pip install` 😱

## Length

5

## Description

In this lightning talk, I will demonstrate how to import packages that have not been installed in a virtual environment. Along the way, we will learn about `importlib` and `sys.modules`.

`pip` is the de-facto Python package manager. We use `pip` to install libraries hosted on the Python Package Index.

pip is a  system used to install and manage software packages written in Python.[4] Many packages can be found in the default source for packages and their dependencies — Python Package Index (PyPI).

In this lightning talk, I will walk thru how we can use the Python standard library to import third-party packages that we d

## Short Bio

Aly Sivji is a Canadian expat living in Chicago. By day, he builds backend systems at Numerator. By night, he is a co-organizer of the Chicago Python Users Group (ChiPy).

## Ideas

- the pull request was being made from behind the firewall // inside of the company?
- there was this project.... had no tests
- context managers
- heartbeat... telltale heart. "ping-pong"
-

Pie-Pee-Eye
pie calvin eye

not PyPy... that's a different thing entirely.

Dustin's Talk https://www.youtube.com/watch?v=AQsZsgJ30AE

```python
import builtins
import inspect


all_exceptions = [
    member
    for name, member in inspect.getmembers(builtins)
    if isinstance(member, type) and issubclass(member, BaseException)
]


class ExceptionHandler:
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            raise random.choice(all_exceptions)
```
