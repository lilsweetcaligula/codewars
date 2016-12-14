#include <stddef.h>

void count_positives_sum_negatives(
  int *values, size_t count, int *positivesCount, int *negativesSum)
{
  *positivesCount = 0;
  *negativesSum = 0;
  
  for (size_t index = 0; index < count; ++index) {
    if (values[index] > 0) {
      ++*positivesCount;
    }    
    else if (values[index] < 0) {
      *negativesSum += values[index];
    }
  }
}