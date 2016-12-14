def hamming(a,b):
  return len(list((True for pair in zip(a, b) if pair[0] != pair[1])))