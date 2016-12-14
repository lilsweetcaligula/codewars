def multiply(*args):
    from operator import mul
    return mul(*args)import operator
multiply = lambda a, b: operator.mul(a, b)