def greet():
    def helper():
        for byte in (104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100):
            yield byte
    return ''.join(chr(byte) for byte in helper())