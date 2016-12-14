pattern = (lambda n: 
    '\n'.join(str(digit) * digit for digit in range(2, n + 1, 2)))