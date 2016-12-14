#include <stdlib.h>

unsigned long long *get_memory_counter(void) {
  static unsigned long long mem_counter;
  return &mem_counter;
}

void *mem_alloc(size_t size) {
  void *buffer = malloc(size);
  if (buffer) {
    *get_memory_counter() += size;
  }
  return buffer;
}

unsigned long long report_total_allocated(void) {
  return *get_memory_counter();
}