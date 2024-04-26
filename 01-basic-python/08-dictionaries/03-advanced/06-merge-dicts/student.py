def merge_dicts(dict1, dict2):
    new_dict = {}
    for i in dict1:
        new_dict[i] = dict1[i]
    
    for i in dict2:    
        new_dict[i] = dict2[i]
    
    return new_dict