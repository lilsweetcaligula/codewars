def repeat_str(count, string):
    # return string * repeat
    from itertools import repeat
    return ''.join(repeat(string, times = count))