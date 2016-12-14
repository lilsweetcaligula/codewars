def calc(x):
    digits1 = ''.join(str(ord(c)) for c in x)
    digits2 = digits1.replace('7', '1')
    return sum(map(int, digits1)) - sum(map(int, digits2))