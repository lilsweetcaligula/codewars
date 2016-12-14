#include <stddef.h>

int get_average(const int *marks, size_t count) {
  int sum = 0;
  for (size_t index = 0; index < count; ++index) {
    sum += marks[index];
  }
  return sum / (int)count;
}