def sum_of_n(n):
  # your code goes here
  #
  sign = abs(n) // (n or 1)
  sequence = [0]
  for step in range(1, abs(n) + 1):
    sequence.append((abs(sequence[-1]) + step) * sign)
  return sequence