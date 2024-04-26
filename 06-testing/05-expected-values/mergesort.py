def split_in_two(ns):
    middle = len(ns) // 2
    return (ns[:middle], ns[middle:])



def merge_sorted(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    result = merge_sorted(sorted_left, sorted_right)
    return result