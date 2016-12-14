def split_odd_and_even(n):
    from itertools import groupby
    digits = map(int, str(n))
    result = []
    for isEven, values in groupby(digits, lambda digit: digit % 2 == 0):
        result.append(int(''.join(map(str, values))))
    return result