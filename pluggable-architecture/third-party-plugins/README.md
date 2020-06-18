# Third Party Plugins

This folder contains my attempt at creating third-party plugins with links to relevant resources.

## Output for Slides

```console
❯ pytest
========================= test session starts =========================
platform darwin -- Python 3.8.1, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: ~/third-party-plugins/pytest-plugins, inifile: pytest.ini
collected 2 items

tests/test_main.py ..                                            [100%]

========================== 2 passed in 1.02s ==========================


❯ pytest --fast
========================= test session starts =========================
platform darwin -- Python 3.8.1, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: ~/third-party-plugins/pytest-plugins, inifile: pytest.ini
collected 2 items / 1 deselected / 1 selected

tests/test_main.py .                                             [100%]

=================== 1 passed, 1 deselected in 0.01s ===================
```

## Resources

https://github.com/hackebrot/earth
https://github.com/hackebrot/earth/blob/europython/tests/conftest.py

## Todo

- implement pytest ago / pytest-relativedelta plugin

```python
@pytest.fixture
def ago():
    def _wrapper(**kwargs):
        return datetime.now(timezone.utc) - relativedelta(**kwargs)

    return _wrapper
````
