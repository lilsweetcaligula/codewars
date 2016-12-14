def sort_list(sort_key, lst):
  return sorted(lst, key = lambda obj: obj[sort_key], reverse = True)