def add_indices(xs):
    indices = []
    for i in range(len(xs)):
        indices.append(i)
    
    final = list(zip(indices, xs))
    return final