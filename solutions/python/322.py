def ip_to_int32(ip):
  bits = ''.join(map(lambda value: bin(value)[2:].zfill(8), map(int, ip.split('.'))))
  return int(bits, base = 2)def ip_to_int32(ip):
  return int(''.join(bin(int(octet))[2:].zfill(8) for octet in ip.split('.')), 2)