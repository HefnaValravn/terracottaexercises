import re
import collections

def check_char_count(string):
    counter = collections.Counter(string)
    return any(count >= 4 for count in counter.values())

def is_valid_password(string):
    if len(string) < 12:
        return False
    
    if not re.search(r'[a-z]', string):
        return False
    
    if not re.search(r'[A-Z]', string):
        return False
    
    if not re.search(r'[0-9]', string):
        return False
    
    if not re.search(r'[+\-*/.@]', string):
        return False
    
    if re.search(r'(.)\1\1', string):
        return False
    
    if check_char_count(string):
        return False
    
    return True


