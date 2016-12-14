#include <stdlib.h>

int hasFive(const int value) 
{
  if (value == 0) {
    return 0;
  }
  else if (abs(value % 10) == 5) {
    return 1;
  }
  return hasFive(value / 10);
}

static int dontGiveMeFiveHelper(const int start, const int end, const int count) 
{
  if (start > end) {
    return count;
  }
  return dontGiveMeFiveHelper(start + 1, end, count + !hasFive(start));
}

int dontGiveMeFive(int start, int end)
{
  return dontGiveMeFiveHelper(start, end, 0);
}