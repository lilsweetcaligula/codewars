def largestPower(N, base = 3):
    from math import log, floor
    return floor(log(N, base)) - (log(N, base) == floor(log(N, base)))