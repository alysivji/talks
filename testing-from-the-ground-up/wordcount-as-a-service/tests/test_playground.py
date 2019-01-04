import pytest


@pytest.mark.skip
def test_failing_example():
    counter = range(10)
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]

    assert counter == my_list


@pytest.fixture
def adder():
    def _wrapper(arg1, arg2):
        # do what we need to
        return arg1 + arg2
    return _wrapper


@pytest.mark.skip
def test_function(adder):
    result = adder(1, 2)
    assert result == 3


@pytest.mark.api_test
@pytest.mark.skip
def test_send_http_post():
    # business logic
    pass
