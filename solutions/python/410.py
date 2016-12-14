def basic_op(op, value1, value2):
    import operator
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }[op](value1, value2)