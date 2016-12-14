def is_prime(num):
  if num % 2 == 0:
      return num == 2
  elif num > 2:
      lim = int(num ** 0.5)
      for candidate in range(3, lim + 1, 2):
          if num % candidate == 0:
              return False
      return True
  return False