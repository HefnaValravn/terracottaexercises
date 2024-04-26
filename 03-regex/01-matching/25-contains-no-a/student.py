import re

def contains_no_a(string):
    return bool(re.search(r'^[^a]*$', string))