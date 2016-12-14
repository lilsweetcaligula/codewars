def group_by_commas(n):
    s = str(n)
    subs = [s[:len(s) % 3]] + [s[start:start + 3] for start in range(len(s) % 3, len(s), 3)]
    return ','.join(filter(lambda sub: len(sub) > 0, subs))