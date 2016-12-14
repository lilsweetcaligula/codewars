def is_digit(n):
    import re
    return re.match(r'^\d\Z', n) != Noneis_digit = lambda n: len(n) > 0 and n in "0123456789"import re

is_digit = lambda n: len(n) > 0 and n in "0123456789"