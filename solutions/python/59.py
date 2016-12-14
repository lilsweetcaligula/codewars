def sc(apple):
    for row, cols in enumerate(apple):
        col = ''.join(cols).find('B')
        if col >= 0:
            return [row, col]
    return [-1, -1]