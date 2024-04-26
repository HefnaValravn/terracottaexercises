def keys_with_value(dictionary, value):
    answer = []
    for i in dictionary:
        if dictionary[i] == value:
            answer.append(i)
    
    return answer