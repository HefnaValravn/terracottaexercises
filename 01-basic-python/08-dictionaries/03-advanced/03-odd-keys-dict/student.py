def odd_keys_dict(dictionary):
    new_dict = {}
    for i in dictionary:
        if i % 2 != 0:
            new_dict[i] = dictionary[i]
    
    return new_dict