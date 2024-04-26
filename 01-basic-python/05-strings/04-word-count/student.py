def word_count(string):
    if not string:
        return 0
    words = string.split(' ')
    return len(words)