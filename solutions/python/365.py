from math import floor

# Standby for ...HORROR.
two_decimal_places = lambda value, decimalPlaces = 2: (floor(value * 10.0 ** decimalPlaces) + 
    (0 if 5 > floor(value * 10.0 ** (decimalPlaces + 1)) % 10 else 1)) / (10.0 ** decimalPlaces)