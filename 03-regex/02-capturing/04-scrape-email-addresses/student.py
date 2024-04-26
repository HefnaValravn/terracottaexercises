import re

def scrape_email_addresses(string):
    return re.findall(r'[A-Za-z0-9.]+@[A-Za-z0-9.]+', string)