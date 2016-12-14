def is_square(n):
    try:
        from math import floor, sqrt
        return floor(sqrt(n)) == sqrt(n)
    except ValueError:
        return False