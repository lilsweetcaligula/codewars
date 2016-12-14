import re

def is_valid_HK_phone_number(number):
    return re.match(r'\A\d{4} \d{4}\Z', number) != None

def has_valid_HK_phone_number(number):
    return re.match(r'.*\d{4} \d{4}.*', number) != None