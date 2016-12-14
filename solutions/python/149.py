def alternate_sq_sum(arr):
    return sum(map(lambda pair: pair[1] if (pair[0] + 1) % 2 else pair[1] ** 2, enumerate(arr)))