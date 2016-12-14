def find_it(seq):
    from collections import Counter
    for value, occurs in Counter(seq).items():
        if occurs % 2:
            return value
    return None