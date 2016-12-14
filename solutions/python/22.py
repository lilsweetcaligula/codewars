def solution(number):
  return sum(candidate for candidate in range(3, number) 
      if candidate % 15 == 0 
          or candidate % 5 == 0 
          or candidate % 3 == 0)