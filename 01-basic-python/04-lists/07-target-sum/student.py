def target_sum(ns, target):
    for i in ns:
        for j in ns:
            if i + i == target or i + j == target or j + j == target:
                return True
            
    return False