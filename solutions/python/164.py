def copy_list(lst):
  if type(lst) != list:
      raise ValueError('lst argument must be a list')
  return lst[:]