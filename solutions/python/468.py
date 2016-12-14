def create_iterator(func, n):
  # TODO: Write code here to return a function 
  # that executes *func*, *n* times on a supplied input
  def chained(value):
      for times in range(n):
          value = func(value)
      return value
  return chained