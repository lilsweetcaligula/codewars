def filter_list(L):
  'return a new list with the strings filtered out'
  return [item for item in L if not isinstance(item, str)]