def square_digits(num):
    return int(''.join(map(str, (int(digit) ** 2 for digit in str(num)))))