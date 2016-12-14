def switcher(arr):
    import string
    chars = (string.ascii_lowercase)[::-1] + '!? '
    return ''.join(map(lambda code: chars[code - 1] if 0 <= code - 1 < len(chars) else '', map(int, arr)))