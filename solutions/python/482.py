def triple_double(num1, num2):
    import re
    digits1, digits2 = (str(num) for num in (num1, num2))
    double_pattern = r'.*(?P<digit>\d)\1'
    triple_pattern = r'.*(?P<digit>\d)\1\1'
    match1 = re.match(triple_pattern, digits1)
    match2 = re.match(double_pattern, digits2)
    if match1 and match2 and match1.group('digit') == match2.group('digit'):
        return 1
    return 0