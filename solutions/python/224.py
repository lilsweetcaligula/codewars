def convertFracts(lst):
  from fractions import gcd
  from functools import reduce
  from math import floor
  leastCommonDivisor = floor(
      reduce(lambda x, y: (x * y) / gcd(x, y), map(lambda frc: frc[1], lst)))
  return list(
      map(lambda frc: [frc[0] * leastCommonDivisor // frc[1], leastCommonDivisor], lst))