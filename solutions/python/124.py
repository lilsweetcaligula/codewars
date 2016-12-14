def sale_hotdogs(n):
    return n * 100 * [1.0, 0.95, 0.9][(5 <= n < 10) + 2 * (n >= 10)]