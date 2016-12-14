def nth_fib(n):
  a, b = 0, 1
  for times in range(n - 1):
      a, b = b, a + b
  return adef nth_fib(n):
  values = [0, 1]
  for times in range(n - len(values)):
      values.append(values[-1] + values[-2])
  return values[n - 1]