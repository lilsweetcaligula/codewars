def get_last_digit(index):
    a, b = 0, 1
    if index < 2:
        return a
    else:
        for times in range(index - 1):
            a, b = b, (a + b) % 10
    return b
    def get_last_digit(index):
    if index < 2:
        return 0
    a, b = 0, 1
    for times in range(index - 1):
        a, b = b, a + b
    return int(str(b)[-1])