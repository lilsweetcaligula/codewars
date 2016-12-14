def to_binary(n):
    from ctypes import c_uint32
    unsigned = c_uint32(n).value
    bits = []
    while True:
        bits.append(unsigned % 2)
        unsigned //= 2
        if unsigned == 0:
           break
    return ''.join(map(str, reversed(bits)))