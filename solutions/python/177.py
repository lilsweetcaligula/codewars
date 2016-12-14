def validate_pin(pin):
    import re
    return re.match(r'\A(?:\d{4}|\d{6})\Z', pin) != None