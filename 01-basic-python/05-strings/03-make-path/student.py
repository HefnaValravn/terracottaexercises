def make_path(parts):
    final = ""
    for i in parts:
        if i == parts[len(parts)-1]:
            final += i
        else:
            final += i + "/"
    return final