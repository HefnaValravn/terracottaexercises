import pytest

from pytest import approx

from mystatistics import average


@pytest.mark.parametrize('ns, expected', [
    ([0.1, 0.1, 0.1], 0.1)
])
def test_average(ns, expected):
    assert average(ns) == approx(expected), f'The average of {ns} is 0.1'