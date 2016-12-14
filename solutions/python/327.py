def longest_consec(strings, count):
  import itertools, operator
  try:
      return max([list(itertools.accumulate(strings[index:index + count]))[-1]
              for index in range(len(strings) - count + 1)], key = len)
  except (ValueError, IndexError):
      return ''