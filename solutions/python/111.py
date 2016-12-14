def factorial(n):
    import functools
    import operator
    return functools.reduce(operator.mul, range(1, n + 1), 1)import sys

MULTIPLIER = 10
sys.setrecursionlimit(sys.getrecursionlimit() * MULTIPLIER)

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)def factorial(n):
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, n + 1), 1)