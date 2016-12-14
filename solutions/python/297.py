pattern = (lambda n:
    '\n'.join(
        ''.join(str(digit) for digit in range(start, n + 1)) 
            for start in range(1, n + 1)))