#include <stddef.h>

int positive_sum(const int *values, size_t count) {
  int sum = 0;
  for (size_t index = 0; index < count; ++index) {
    if (values[index] > 0) {
      sum += values[index];
    }
  }
  return sum;
}