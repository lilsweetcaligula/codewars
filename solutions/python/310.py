def numbers_with_digit_inside(x, d):
    from functools import reduce
    from operator import add, mul
    numbers = [value for value in range(1, x + 1) if str(d) in str(value)]
    return [len(numbers), reduce(add, numbers, 0), reduce(mul, numbers, 1 if numbers else 0)]