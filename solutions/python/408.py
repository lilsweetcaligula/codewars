def series_sum(n):
    # Happy Coding ^_^
    # > Thanks, You too ^_^
    value = 0.0
    divisor = 1.0
    step = 3.0
    for _ in range(n):
        value += 1.0 / divisor
        divisor += step
    return '%.2f' % value