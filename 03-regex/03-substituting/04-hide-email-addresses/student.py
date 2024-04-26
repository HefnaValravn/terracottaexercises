import re

def hide_email_addresses(string):
    def replace(match):
        email = match.group(0)
        return '*' * len(email)
    

    return re.sub(r'[A-Za-z0-9.]+@[A-Za-z0-9.]+', replace, string)