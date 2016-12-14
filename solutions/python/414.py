def binary_array_to_number(bits):
    return int("".join(str(bit) for bit in bits), base=2)