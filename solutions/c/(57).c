#include <stdlib.h>
#include <string.h>

typedef void* (*Function)(const void*, const void*);

void *lzip(
  const void *a, size_t a_count, size_t a_item_size,
  const void *b, size_t b_count, size_t b_item_size,
  size_t result_item_size, Function func) 
{
  size_t min_count = a_count < b_count ? a_count : b_count;
  
  void *result = malloc(result_item_size * min_count);
  if (result) {  
    for (size_t index = 0; index < min_count; ++index) {
      const void *a_item = (char*)a + index * a_item_size;
      const void *b_item = (char*)b + index * b_item_size;
      
      void *dest = (char*)result + index * result_item_size;
      void *item = func(a_item, b_item);
      
      (void)memcpy(dest, &item, result_item_size);
    }
  }
  return result;
}