def rotate(xs, n):
    n = n % len(xs)

    xs[:] = xs[n:] + xs[:n]
    return xs