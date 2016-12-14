def narcissistic( value ):
    digits = map(int, str(value))
    return value == sum(digit ** len(digits) for digit in digits)