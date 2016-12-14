def gap(num):
    from itertools import groupby
    return max(
        [len(list(group)) for value, group in groupby(bin(num)[2:].rstrip('0')) if value == '0'] or [0])