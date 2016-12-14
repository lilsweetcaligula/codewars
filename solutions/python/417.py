def GreatestCommonDivisor(n, m):
    while m > 0: 
        n, m = m, n % m
    return n

def LeastCommonMultiple(n, m):
    try:
        return (n * m) / GreatestCommonDivisor(n, m)
    except ZeroDivisionError:
        return 0

def sum_differences_between_products_and_LCMs(pairs):
    result = 0
    for pair in pairs:
        a, b = pair
        product = a * b
        leastCommonMultiple = LeastCommonMultiple(a, b)
        result += product - leastCommonMultiple
    return result