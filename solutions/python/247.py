def binary_to_string(binary):
    return ''.join(chr(int(binary[start:start + 8], 2)) for start in range(0, len(binary), 8))
    