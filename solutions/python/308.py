# Inspired by AntraxMiope

import re

pair_zeros = (lambda arr, *_:    
    map(int, re.sub('(0[^0]*)0', '\\1', "".join(str(value) for value in arr))))def pair_zeros(arr, *_):
  result = []
  count = 0
  for value in arr:
    if value == 0:
      count = (count + 1) % 2
    if value != 0 or count != 0:
      result.append(value)
  return resultdef pair_zeros(arr, *_):
  zeroValueIndices = [index for index, value in enumerate(arr)
                        if value == 0]
  excludedIndices = set(zeroValueIndices[1::2])
  return [value for index, value in enumerate(arr)
            if index not in excludedIndices]def pair_zeros(*arr):
  arr = arr[0]
  result = []
  count = 0
  for value in arr:
    if value == 0:
      count = (count + 1) % 2
    if value != 0 or count != 0:
      result.append(value)
  return resultdef pair_zeros(*arr):
  arr = arr[0]
  zeroValueIndices = [index for index, value in enumerate(arr)
                        if value == 0]
  excludedIndices = set(zeroValueIndices[1::2])
  return [value for index, value in enumerate(arr)
            if index not in excludedIndices]