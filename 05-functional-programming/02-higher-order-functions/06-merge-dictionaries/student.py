def merge_dictionaries(d1, d2, merge_function):
    answer = dict(d1)
    for k, v in d2.items():
        if k in answer:
            answer[k] = merge_function(answer[k], v)
        else:
            answer[k] = v
    
    return answer
