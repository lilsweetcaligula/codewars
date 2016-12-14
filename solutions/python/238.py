class Converter:
    @staticmethod
    def to_hex(s):
      return ''.join(hex(ord(char))[2:] for char in s)
    
    @staticmethod
    def to_ascii(h):
      return ''.join(chr(int(h[start:start + 2], base = 16)) for start in range(0, len(h), 2))