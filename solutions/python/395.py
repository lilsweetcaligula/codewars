def order(sentence, separator = ' '):
  from re import search
  words = sentence.split()
  return separator.join(sorted(words, key = lambda x : search(r'\d', x).group()))