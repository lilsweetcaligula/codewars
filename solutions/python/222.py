def get_number_of_squares(n):
    value = 1
    count = 0
    total = 0
    while total + value ** 2 < n:
        total += value ** 2
        value += 1
        count += 1
    return countdef get_number_of_squares(value):
  result = []
  candidate = 1
  # candidate * (candidate - 1) / 2 == sum(range(candidate))
  while sum(result) + candidate ** 2 < value:
    result.append(candidate ** 2)
    candidate += 1
  return len(result)