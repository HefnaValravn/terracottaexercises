def drop_nth(xs, n):
    first = xs[:n]
    last = xs[n+1:]

    return [*first, *last]