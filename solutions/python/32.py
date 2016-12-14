def divisors(n):
    return len([candidate for candidate in range(1, n + 1) if n % candidate == 0])