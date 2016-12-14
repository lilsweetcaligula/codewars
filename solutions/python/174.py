def reverse(s):
  return s if len(s) < 2 else s[-1] + reverse(s[:-1])