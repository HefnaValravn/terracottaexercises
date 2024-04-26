from math import floor, ceil
def median(ns):
    ns = sorted(ns)
    n = len(ns)
    if len(ns) % 2 == 0:
        return (ns[n // 2] + ns[n // 2 - 1]) / 2
    else:
        return (ns[len(ns)//2])