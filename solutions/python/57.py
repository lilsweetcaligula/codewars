def calculate(n1, n2, o):
    import operator
    operator_lookup = {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.floordiv
    }
    result = operator_lookup[o](int(n1, base = 2), int(n2, base = 2))
    sign = 1 if result > 0 else -1 if result < 0 else 0
    return '{}{}'.format('-' if sign < 0 else '', bin(abs(result))[2:])