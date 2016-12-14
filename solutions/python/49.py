def two_decimal_places(number, ndigits = 2):
    return int(number * 10 ** ndigits) / (10.0 ** ndigits)