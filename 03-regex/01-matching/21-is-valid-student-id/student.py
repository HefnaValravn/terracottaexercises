import re
def is_valid_student_id(string):
    count_r = string.lower().count('r')
    count_s = string.lower().count('s')
    return (count_r == 1) ^ (count_s == 1) and bool(re.fullmatch(r'^(.)\d{7}$', string))
