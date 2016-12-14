def whitespace(string):
    import re
    return re.match(r'^\s*\Z', string) != None