def vowel_shift(text,n):
  if not text or not n:
    return text
  from itertools import chain, cycle
  vowels = set('aeoui')
  text_vowels = [char for char in text if char.lower() in vowels]
  n = n % len(text_vowels) if len(text_vowels) > 0 else 0
  vowels_iterator = cycle(chain(text_vowels[-n:], text_vowels[:-n]))
  return ''.join(char if char.lower() not in vowels else next(vowels_iterator)
                 for char in text)