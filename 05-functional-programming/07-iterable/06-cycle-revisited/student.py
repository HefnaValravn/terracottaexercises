def cycle(xs):
    while True:
        for i in range(len(xs)):
            yield xs[i]