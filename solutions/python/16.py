def array_diff(a, b):
    lookup = set(b)
    return [value for value in a if value not in lookup]