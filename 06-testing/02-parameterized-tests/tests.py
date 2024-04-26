import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    ('(((())))'),
    ('(())()'),
    ('()'),
    ('(())')
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f'Set of parentheses {string} is a correct set'




@pytest.mark.parametrize('string', [
    ('(((())'),
    (')'),
    ('((()())()(()'),
    (')))')
])
def test_nonmatching_parentheses(string):
    assert not matching_parentheses(string), f'Set of parentheses {string} is not a correct set'