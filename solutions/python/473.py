def persistence(number):
    from operator import mul
    count = 0
    while number >= 10:
        number = reduce(mul, map(int, str(number)))
        count += 1
    return count