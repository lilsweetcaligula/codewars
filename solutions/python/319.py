def initializeNames(name):
  names = name.split()
  names[1:-1] = map(lambda x: "".join(x[:1]) + '.', names[1:-1])
  return ' '.join(names)def initializeNames(name):
  names = name.split()
  return (' '.join(
      name if index == 0 or index == len(names) - 1 
      else name.strip()[0] + '.' 
      for index, name in enumerate(names)))
  