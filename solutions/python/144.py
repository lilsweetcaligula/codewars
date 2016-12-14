def triple_shiftian(base, n):
    for times in xrange(n - len(base) + 1):
        next_number = 4 * base[-1] - 5 * base[-2] + 3 * base[-3]
        base.append(next_number)
    return base[n]