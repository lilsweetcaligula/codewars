def next_pal(val):
    s = str(val)
    mid = len(s) // 2
    isLengthOdd = bool(len(s) % 2)
    if isLengthOdd:
        mid += 1
    for half in (int(s[:mid]), int(s[:mid]) + 1):        
        candidate = int(
        str(half) + ''.join(reversed(str(half)[:-1 if isLengthOdd else len(str(half))])))
        if candidate > val:
            return candidate
    return candidate