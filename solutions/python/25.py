def is_divisible(n, *args):
    return all(n % arg == 0 for arg in args)