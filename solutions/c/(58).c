#include <stdio.h>

char *series_sum(const size_t n) {
  const size_t count = 32;
  char *buffer = (char*)malloc(sizeof(char) * count);
  if (buffer) {  
    double value = 0.0;
    int divisor = 1;
    int step = 3;
    for (size_t times = 0; times < n; ++times) {
      value += 1.0 / divisor;
      divisor += step;
    }
    
    (void)snprintf(buffer, count, "%.2lf", value);
  }
  return buffer;
}