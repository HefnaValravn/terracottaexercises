from itertools import pairwise

def total_distance(path, distance):
    pairs = pairwise(path)
    return sum(distance(i, j) for i, j in pairs)