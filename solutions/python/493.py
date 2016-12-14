def isValidWalk(walk):
    if len(walk) != 10:
        return False
    lookup = {
        'n': lambda x, y: [x, y + 1],
        's': lambda x, y: [x, y - 1],
        'w': lambda x, y: [x - 1, y],
        'e': lambda x, y: [x + 1, y],
    }
    x = y = 0
    for direction in walk:
        x, y = lookup[direction](x, y)
    return x == y == 0