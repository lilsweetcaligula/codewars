#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef bool (*Predicate)(const int*);

int *dropWhile(
  const int *values, 
  size_t     count,
  Predicate  pred, 
  size_t     *pResultCount)
{
  *pResultCount = 0;
  
  if (values)
  {
    size_t index = 0;  
    while (index < count) {
      if (!pred(&values[index])) {
        break;
      }
      ++index;
    }
    
    const size_t takeCount = count - index;
    *pResultCount = takeCount;
    
    if (takeCount > 0) {
      int *buffer = malloc(sizeof(values[0]) * takeCount);
      if (buffer) {
        (void)memcpy(buffer, &values[index], sizeof(values[0]) * takeCount);
      }
      return buffer;
    }
  }
  return NULL;
}