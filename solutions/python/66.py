def validate_ean(code):
    return sum(
        int(digit) if index % 2 else int(digit) * 3 
            for index, digit in enumerate(code, start = 1)) % 10 == 0