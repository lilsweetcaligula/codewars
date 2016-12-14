#include <stddef.h>

int compareIntegers(const int *lhs, const int *rhs) {
  return *lhs - *rhs;
}

int* completeSeries(int* arr, int arrLength)
{
  qsort(arr, (size_t)arrLength, sizeof(int), compareIntegers);
  
  for (int index = 1; index < arrLength; ++index) {
    if (arr[index] == arr[index - 1]) {
      return (int*)calloc(1, sizeof(int));
    }
  }
  
  int maxValue = arr[arrLength - 1];
  int *result = (int*)malloc(sizeof(int) * (maxValue + 1));
  if (result) {
    for (int index = 0; index <= maxValue; ++index) {
      result[index] = index;
    }
  }
  return result;
}