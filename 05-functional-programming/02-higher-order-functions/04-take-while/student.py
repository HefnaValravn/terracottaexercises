def take_while(xs, is_negative):
    for x in xs:
        if not is_negative(x):
            return (xs[:xs.index(x)], xs[xs.index(x):])
    
    return (xs, [])