#include <stddef.h>

size_t *monkey_count(size_t n, size_t *pResultCount) {
  *pResultCount = 0;
  size_t *monkeys = (size_t*)malloc(sizeof(size_t) * n);
  if (monkeys) {
    while (*pResultCount < n) {
      monkeys[*pResultCount] = *pResultCount + 1;
      ++*pResultCount;
    }
  }
  return monkeys;
}