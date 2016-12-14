def is_valid(idn):
    import re
    return re.match(r'\A[A-Za-z_$][A-Za-z_0-9$]*\Z', idn) != None