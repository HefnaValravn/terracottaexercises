def contains_duplicates(xs):
    unique = set(xs)
    return len(unique) != len(xs)