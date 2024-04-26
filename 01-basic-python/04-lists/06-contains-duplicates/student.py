def contains_duplicates(xs):
    check = []
    for i in xs:
        if i in check:
            return True
        else:
            check.append(i)
    
    return False