def add(a,b):
    i, j = len(a) - 1, len(b) - 1
    result_bits = []
    carry = 0
    while i >= 0 or j >= 0:
        a_bit = b_bit = 0
        if i >= 0:
            a_bit = 1 if a[i] == '1' else 0
            i -= 1
        if j >= 0:
            b_bit = 1 if b[j] == '1' else 0
            j -= 1
        addition = a_bit + b_bit
        result_bit = (addition + carry) % 2
        result_bits.append('1' if result_bit else '0')
        carry = (carry + addition) // 2
    if carry > 0:
        result_bits.append('1' if carry else '0')
    return ''.join(reversed(result_bits)).lstrip('0') or '0'