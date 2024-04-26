def indices_of(xs, is_odd):
    answer = []
    for x in xs:
        if is_odd(x):
            answer.append(xs.index(x))
    
    return answer