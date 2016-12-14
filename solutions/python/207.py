def next_version(version):
    digits = list(map(int, version.split('.')))
    carry = 1
    for index in reversed(range(len(digits))):
        digits[index] += carry
        carry = digits[index] // 10
        if index != 0:
            digits[index] %= 10
    return '.'.join(map(str, digits))