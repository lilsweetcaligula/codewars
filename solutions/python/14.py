def digital_root(n):
    digits = list(map(int, str(n)))
    if len(digits) <= 1:
        return n
    return digital_root(sum(digits))