def factors(x):
    if type(x) != int or x < 1:
        return -1
    factors = []
    factor = x
    while factor > 0:
        if x % factor == 0:
            factors.append(factor)
        factor -= 1
    return factors