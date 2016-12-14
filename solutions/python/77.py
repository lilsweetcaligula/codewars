def circleArea(r, ndigits = 2):
    from math import pi
    if type(r) not in (int, float) or r < 0:
        return False
    return round(r ** 2 * pi, ndigits)