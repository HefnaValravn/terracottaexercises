def matching_parentheses(string):
    track = []
    for char in string:
        if char == '(':
            
            track.append(char)
        elif char == ')':
            if not track:
                return False
            if track[-1] != '(':
                return False
            else:
                track.pop()
    return len(track) == 0
