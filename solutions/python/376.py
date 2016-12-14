def max_product(values: list) -> int:
    from operator import mul
    firstMax = max(values)
    secondMax = float("-inf")
    for value in values:
        if secondMax < value < firstMax:
            secondMax = value
    return mul(firstMax, secondMax)