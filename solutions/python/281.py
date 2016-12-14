def in_array(a1, a2):
  source = ''.join(a2)
  return sorted(list(set(substring for substring in a1 if substring in source)))