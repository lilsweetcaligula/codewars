def climb(n):
    return [1] if n == 1 else climb(n // 2) + [n]def climb(n):
    result = []
    while n >= 1:
        result.append(n)
        n //= 2
    return result[::-1]