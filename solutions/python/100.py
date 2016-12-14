def validSolution(sudokuTable):
  from collections import Counter
  from itertools import chain  
  legalValues = Counter(range(1, 11))
  
  # Check the whole grid.
  for line in chain(sudokuTable, zip(*sudokuTable)):    
    if len(Counter(line) - legalValues) > 0:
      return False
      
  # Check the 3x3 grids.
  for rowNumber in range(0, len(sudokuTable), 3):
    for colNumber in range(0, len(sudokuTable), 3):
      grid = chain(*((sudokuTable[_][colNumber:colNumber + 3]) 
          for _ in range(rowNumber, rowNumber + 3)))
          
      if len(Counter(grid) - legalValues) > 0:
          return False
      
  return True