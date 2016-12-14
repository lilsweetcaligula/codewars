def caffeineBuzz(n):
    return([
        'mocha_missing!', 
        'Coffee' + ('Script' if n % 2 == 0 else ''),
        'Java' + ('Script' if n % 2 == 0 else ''), 
        ][(n % 4 == 0) or 2 * (n % 3 == 0)])