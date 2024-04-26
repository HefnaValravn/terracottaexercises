import re

def two_or_more_abc(string):
    pattern = r'(abc).*\1'
    return bool(re.fullmatch(pattern, string))