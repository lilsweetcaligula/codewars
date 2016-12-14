#include <stddef.h>

double round(double value) {
  if (value - (int)value < 0.5) {
    return (double)((int)value);
  }
  return (double)((int)value + 1);
}

int averageHelper(const int *values, size_t count, size_t currentCount, double currentSum);

int average(const int *values, size_t count) {
  return averageHelper(values, count, count, 0.0);
}

int averageHelper(const int *values, size_t count, size_t currentCount, double currentSum) {
  if (currentCount == 0) {
    return (int)round(currentSum / count);
  }
  return averageHelper(values + 1, count, currentCount - 1, currentSum + *values);
}