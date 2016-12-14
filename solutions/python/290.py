def sumsquares(iterable):
    total = 0
    for item in iterable:
        action = (
            sumsquares if hasattr(item, '__iter__') 
            else lambda x: x ** 2)
        total += action(item)
    return total