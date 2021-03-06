#include <assert.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

int compareIntegers(const int *lhs, const int *rhs) {
  return *lhs - *rhs;
}

const char* meanVsMedian(int *numbers, size_t numbersSize) {
  // Make sure the count is odd or zero in accordance with the problem spec.
  assert(numbersSize == 0 || numbersSize % 2);
  
  if (!numbers || numbersSize == 0) {
    return "";
  }
  
  // Sorting is done in-place. While it would generally be better to create
  // a copy of the numbers array, the spec allows to operate directly on
  // the numbers array.
  (void)qsort(numbers, numbersSize, sizeof(int), compareIntegers);
  const int median = numbers[numbersSize / 2];
  
  double sum = 0.0;
  for (size_t index = 0; index < numbersSize; ++index) {
    sum += numbers[index];
  }
    
  const double mean = sum / numbersSize;  
  if (fabs(mean - median) <= DBL_EPSILON) {
    return "same";
  }
  return median > mean ? "median" : "mean";
}
