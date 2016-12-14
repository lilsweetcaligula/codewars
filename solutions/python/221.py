def minimum_sum(values, n):
  '''sum the n smallest integers in the array values (not necessarily ordered)'''
  return sum(sorted(values)[:n] or [0])

def maximum_sum(values, n):
  '''sum the n largest integers in the array values (not necessarily ordered)'''
  return sum(sorted(values, reverse = True)[:n] or [0])