def beetle_juice(name, times = 3):
    from itertools import repeat
    return '  '.join(repeat(name, times))