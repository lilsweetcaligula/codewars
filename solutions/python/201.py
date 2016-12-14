def insert_dash(num):
    from itertools import groupby
    return ''.join(
        '-'.join(group) if label else ''.join(group) 
            for label, group in groupby(
                list(str(num)), key = lambda item: int(item) % 2))