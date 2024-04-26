import pytest
import itertools
from mergesort import *

@pytest.mark.parametrize('ns', [
    list(range(k) for k in range(100))
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1
    
    

@pytest.mark.parametrize('left', [
    [1, 3, 5],
    [],
    [5, 6, 7],
    [25, 27, 30],
    [3, 5, 6]
])

@pytest.mark.parametrize('right', [
    [20, 26, 29, 30, 31],
    [3, 5],
    [],
    [12, 13, 15, 16, 17, 19],
    [26, 27]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)
    
    
@pytest.mark.parametrize('expected, ns', [
    (ns, list(permutation))
    for ns in [[], [1], [1, 2], [1, 4, 4, 6], [1, 2, 2, 4, 6, 9]]
    for permutation in itertools.permutations(ns)
])
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected