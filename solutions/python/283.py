def get_length_of_missing_array(array_of_arrays):
  lengths = [len(sub) for sub in array_of_arrays or [] if sub] or [0]
  return(
      array_of_arrays 
      and all(array_of_arrays) 
      and sum(range(min(lengths), max(lengths) + 1)) - sum(lengths) 
      or 0)def get_length_of_missing_array(array_of_arrays):
  if not array_of_arrays or not all(array_of_arrays):
      return 0
  lengths = [len(sub) for sub in array_of_arrays]
  return set(range(min(lengths), max(lengths) + 1)).difference(lengths).pop()