# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically

def letter_frequency(text):
  from collections import Counter
  frequencies = Counter(char.lower() for char in text if char.isalpha()).items()
  return sorted(
      sorted(frequencies, key = lambda pair: pair[0]), 
      key = lambda pair: pair[1], reverse = True)