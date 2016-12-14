def unique_in_order(iterable):
    from itertools import groupby
    return [item for item, _ in groupby(iterable)]