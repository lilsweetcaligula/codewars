def signed_eight_bit_number(number):
    import re
    match = re.match(r'^(0)\Z|^((\+|-)?([1-9]\d+))\Z|^(-?[1-9])\Z', number)
    if match:
        value = int(match.group(0))
        return -128 <= value <= 127
    return False