def power(L):
    from itertools import combinations, chain
    return [list(sub) for sub in chain(*[combinations(L, r) for r in range(len(L) + 1)])]