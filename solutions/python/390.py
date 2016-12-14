def logical_calc(array, op):
    import operator, functools
    op = (op == "AND" and operator.and_ 
        or op == "OR" and operator.or_
        or operator.xor)
    return functools.reduce(op, array)