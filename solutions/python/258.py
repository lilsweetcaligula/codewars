def binary_gcd(x, y):
    import fractions
    return bin(fractions.gcd(x, y)).count('1')