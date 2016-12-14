#include <stdlib.h>
#include <float.h>
#include <math.h>

int compareIntegers(const int *lhs, const int *rhs) {
  return *lhs - *rhs;
}

const char* meanVsMedian(int *numbers, size_t numbersSize) {
  if (!numbers || numbersSize == 0) {
    return "";
  }
  
  (void)qsort(numbers, numbersSize, sizeof(int), compareIntegers);
  int median = numbers[numbersSize / 2];
  
  double sum = 0.0;
  for (size_t index = 0; index < numbersSize; ++index) {
    sum += numbers[index];
  }
  double mean = sum / numbersSize;
  
  if (fabs(mean - median) <= DBL_EPSILON) {
    return "same";
  }
  return median > mean ? "median" : "mean";
}