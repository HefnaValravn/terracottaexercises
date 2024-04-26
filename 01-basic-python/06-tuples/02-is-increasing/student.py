def is_increasing(ns):
    if not ns:
        return True
    previous = ns[0]
    for i in ns:
        if i < previous:
            return False
        
        previous = i
    
    return True
