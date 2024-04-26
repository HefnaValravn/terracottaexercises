def group_by(xs, key_function):
    answer = {}
    for x in xs:
        key = key_function(x)
        if key not in answer:
            answer[key] = []
        answer[key].append(x)
    return answer