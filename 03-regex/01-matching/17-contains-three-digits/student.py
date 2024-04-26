import re

def contains_three_digits(string):
    pattern = r'.*\d.*\d.*\d.*'
    return bool(re.match(pattern, string))