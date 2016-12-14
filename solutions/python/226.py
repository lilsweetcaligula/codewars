def scale(s, k, n):
  if not s.strip():
      return ''
  lines = s.split('\n')
  return '\n'.join(
      ''.join(char * k for char in line) 
          for line in lines for i in range(n))