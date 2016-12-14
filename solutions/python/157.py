def get_larger_numbers(a, b):
    return list(map(lambda n, m: n if n > m else m, a, b))
