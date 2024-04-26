import re

def is_dna(string):
    if len(string) == 0:
        return True
    pattern = r'^[AGTC]+$'
    return bool(re.match(pattern, string))
    