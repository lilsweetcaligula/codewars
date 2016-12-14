class HTMLGen:
  def __getattr__(self, tag):
      if tag == 'comment':
          left  = '<!--'
          right = '-->'
      else:
          left  = '<{}>'.format(tag)
          right = '</{}>'.format(tag)
      return lambda text: '{left}{text}{right}'.format(
          left = left, 
          text = text, 
          right = right)