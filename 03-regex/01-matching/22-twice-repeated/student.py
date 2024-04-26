import re

def twice_repeated(string):
    if " " in string and len(string) % 2 == 0:
        return True
    return bool(re.search(r'^([a-zA-Z0-9]+)\1$', string))