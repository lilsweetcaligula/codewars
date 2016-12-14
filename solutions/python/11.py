def validPhoneNumber(phoneNumber):
    import re
    pattern = r'\A\(\d{3}\) \d{3}-\d{4}\Z'
    return re.match(pattern, phoneNumber) != None