import re

def one_or_more_a(string):
    pattern = r'a+'
    return bool(re.fullmatch(pattern, string))