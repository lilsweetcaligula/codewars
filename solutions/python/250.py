def fisHex(name):
    import operator
    import functools
    hexChars = filter(lambda char: char.lower() in 'abcdef', name)
    hexChars = map(lambda char: int(char, base = 16), hexChars)
    return functools.reduce(operator.xor, hexChars, 0)