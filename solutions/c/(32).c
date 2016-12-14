#include <stdlib.h>

int compareIntegers(const int *lhs, const int *rhs) {
  return *lhs - *rhs;
}

int sum(int* numbers, int numbersCount)
{
  (void)qsort(numbers, numbersCount, sizeof(int), compareIntegers);
  
  int result = 0;
  for (int index = 1; index < numbersCount - 1; ++index) {
    result += numbers[index];
  }
  return result;
}