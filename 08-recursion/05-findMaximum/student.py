def findMaximum(list):
    if len(list) == 0:
        raise IndexError
    if len(list) == 1:
        return list[0]
    else:
        if list[0] >= list[1]:
            list.remove(list[1])
        else:
            list.remove(list[0])
        
        return findMaximum(list)
    