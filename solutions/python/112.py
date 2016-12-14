def is_bouncy(number):
    digits = list(str(number))
    return digits != sorted(digits) and digits != sorted(digits, reverse = True)
    