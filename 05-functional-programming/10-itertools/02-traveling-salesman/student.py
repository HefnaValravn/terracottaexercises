from itertools import permutations, pairwise

def find_shortest_path(distance, city_count):
    paths = ([0, *p, 0] for p in permutations(range(1, city_count)))
    shortest = min(paths, key=lambda path: sum(distance(a,b) for a, b in pairwise(path)))
    return shortest