def to_integer(string):
  import re
  patterns = {    
    r'^(\+|\-)?0b[0-1]+\Z': 2,
    r'^(\+|\-)?0o[1-7]+\Z': 8,
    r'^(\+|\-)?[0-9]+\Z': 10,
    r'^(\+|\-)?0x[0-9A-Fa-f]+\Z': 16,
  }
  for pattern in patterns:
    if re.match(pattern, string):
      return int(string, base = patterns[pattern])
  return None