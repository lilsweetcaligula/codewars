def is_narcissistic(i):
    digits = [int(digit) for digit in str(i)]
    return i == sum(digit ** len(digits) for digit in digits)