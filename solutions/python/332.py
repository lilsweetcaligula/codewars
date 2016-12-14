rgb = (lambda r, g, b: ('{:02X}' * 3).format(
    max(0, min(255, r)), 
    max(0, min(255, g)), 
    max(0, min(255, b))
    ))def rgb(r, g, b):
  constrain = lambda x : 0 if x < 0 else x - x % 255 + x * (x < 255)
  return "".join((
      hex(constrain(r))[2:].zfill(2), 
      hex(constrain(g))[2:].zfill(2), 
      hex(constrain(b))[2:].zfill(2)
  )).upper()