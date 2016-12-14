#include <stdlib.h>
#include <string.h>

struct Item {
  int index;
  int value;
};

int compareItemsByValue(const struct Item *lhs, const struct Item *rhs) {
  return lhs->value - rhs->value;
}

int compareItemsByIndex(const struct Item *lhs, const struct Item *rhs) {
  return lhs->index - rhs->index;
}

int *distinct(const int *values, size_t count, size_t *pResultCount) 
{
  *pResultCount = 0;
  if (values && count > 0)
  {  
    struct Item items[count];
  
    // Fill items with each array item's value and its index.
    for (size_t index = 0; index < count; ++index) {
      items[index].index = index;
      items[index].value = values[index];
    }
    
    // Sort items by their value.
    qsort(items, count, sizeof(items[0]), compareItemsByValue);
    
    // Now that the items are sorted by value, each duplicate 
    // will follow one another. Now we can remove duplicates in
    // the items' array in O(n).
    size_t slow = 0, fast = 1;
    while (fast < count) {
      if (items[slow].value != items[fast].value) {
        ++slow;
        items[slow] = items[fast];
      }
      ++fast;
    }
    *pResultCount = slow + 1;
    
    // Sort the first *pResultCount items back by the index, 
    // thus restoring the values' original order.
    // At this point, we have exactly *pResultCount unique values.
    qsort(items, *pResultCount, sizeof(items[0]), compareItemsByIndex);

    // Retrieve the unique values from the items. Please keep in
    // mind that we have exactly *pResultCount unique values at
    // this point.
    int *buffer = (int*)malloc(sizeof(values[0]) * *pResultCount);
    if (buffer) {
      for (size_t index = 0; index < *pResultCount; ++index) {
        buffer[index] = items[index].value;
      }
    }
    return buffer;
  }
  return NULL;
}