def find_next_power(val, power):
    from math import ceil
    return ceil(val ** (1.0 / power)) ** power