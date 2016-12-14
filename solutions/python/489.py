def autocorrect(input):
    import re
    pattern = r'\b(you+|u)\b'
    return re.sub(pattern, 'your sister', input, flags = re.IGNORECASE)