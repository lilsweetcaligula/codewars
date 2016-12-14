def square_it(digits):
    from math import ceil
    from math import sqrt
    digits = str(digits)
    length = len(digits)
    square_root = sqrt(length)
    if ceil(square_root) ** 2 == length:
        chunk_size = ceil(square_root)
        return '\n'.join(
            digits[start:start + chunk_size] 
                for start in range(0, len(digits), chunk_size))
    return 'Not a perfect square!'