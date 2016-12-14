def unique(integers):
    # This one's a one-liner but not efficient.
    # Due to the O(n) nature of the "index" method of "list" type,
    # Time complexity is as bad as O(n^2)
    return sorted(set(integers), key = lambda integer: integers.index(integer))