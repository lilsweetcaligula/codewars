score = lambda n: 2 ** n.bit_length() - 1def score(n):
    if n == 0:
        return 0
    mask = 1
    while mask <= n:
        mask <<= 1
    return mask - 1