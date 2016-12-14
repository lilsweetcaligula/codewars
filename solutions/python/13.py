def reverse_words(s):
  import re
  pattern = r'\S+'
  words = re.findall(pattern, s)
  return re.sub(pattern, '{}', s).format(*(word[::-1] for word in words))