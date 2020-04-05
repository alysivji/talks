# Life without `pip install` 😱

## Length

5

## Description

In this lightning talk, I will demonstrate how to import packages that have not been installed in a virtual environment.

## Short Bio

Aly Sivji is a Canadian expat living in Chicago. By day, he builds backend systems at Numerator. By night, he is a co-organizer of the Chicago Python Users Group (ChiPy).

## Ideas

- the pull request was being made from behind the firewall // inside of the company?
- there was this project.... had no tests
- context managers
- heartbeat... telltale heart. "ping-pong"

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
