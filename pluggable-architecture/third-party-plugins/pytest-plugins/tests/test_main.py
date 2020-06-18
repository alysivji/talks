import pytest
from src.main import calc_fast, calc_slow


def test_calc_fast():
    calc_fast()
    assert True


@pytest.mark.slow
def test_calc_slow():
    calc_slow()
    assert True
