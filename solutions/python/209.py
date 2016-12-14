def two_sum(values, result):
    from collections import OrderedDict
    lookup = OrderedDict({ value: index for index, value in enumerate(values) })
    for index, x in enumerate(values):
        y = result - x
        if y in lookup:
            return [index, lookup[y]]
    return [-1, -1]