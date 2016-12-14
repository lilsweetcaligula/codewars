def diff(pairs):
    from functools import reduce
    pairs = filter(lambda pair: reduce(lambda a, b: abs(a - b) != 0, map(int, pair.split('-'))), pairs)
    return len(pairs) and max(pairs, key = lambda pair: reduce(lambda a, b: abs(a - b), map(int, pair.split('-'))))