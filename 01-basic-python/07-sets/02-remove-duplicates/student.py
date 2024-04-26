def remove_duplicates(xs):
    seen = set()
    result = []
    for i in xs:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result