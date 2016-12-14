def shades_of_grey(n):
  if n < 0:
      return []
  n = min(254, n)
  return ['#' + ''.join(hex(i)[2:].zfill(2) for j in range(3)) for i in range(1, n + 1)]