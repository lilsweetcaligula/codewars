def dig_pow(n, p):
    digits = tuple(map(int, str(n)))
    powers = range(p, p + len(digits))
    candidate = sum(
      digit ** power for digit, power in zip(digits, powers))
    return candidate // n if (candidate % n== 0) else -1def dig_pow(value, power):
  from itertools import permutations
  digits = tuple(map(int, str(value)))
  for power_permutation in permutations(range(power, power + len(digits))):
    candidate = sum(digit ** power for digit, power in zip(digits, power_permutation))
    if candidate % value == 0:
      return candidate // value
  return -1 