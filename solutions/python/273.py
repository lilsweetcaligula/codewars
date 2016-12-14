def cheapest_quote(n, ndigits = 2):
    costs = { 1 : 0.10, 5 : 0.49, 10 : 0.97, 20 : 1.93, 40 : 3.85 }
    total = 0.0
    while n > 0:
        count = list(filter(lambda cost: cost <= n, (1, 5, 10, 20, 40))).pop()
        total += costs[count] * (n // count)
        n %= count
    return round(total, ndigits)