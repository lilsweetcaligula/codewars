#include <stdlib.h>

int find_outlier(const int *values, size_t count) {
  int oddCount = 0;
  int evenCount = 0;
  for (size_t index = 0; index < count; ++index) {
    if (values[index] % 2) {
      ++oddCount;
    } else {
      ++evenCount;
    }
  }
  
  int parity = evenCount > oddCount;
  for (size_t index = 0; index < count; ++index) {
    if (abs(values[index] % 2) == parity) {
      return values[index];
    }
  }
  return *values;
}