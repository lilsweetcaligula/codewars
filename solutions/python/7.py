def string_parse(s):
  if type(s) != str:
      return 'Please enter a valid string'
  import itertools
  result = ''
  for char, chars in itertools.groupby(s):
    group = ''.join(chars)
    result += '{}{}'.format(
        group[:2], 
        '[' + group[2:] + ']' if len(group) > 2 else '')
  return result