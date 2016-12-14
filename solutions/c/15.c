#include <stddef.h>

unsigned binary_array_to_numbers(const unsigned *bits, size_t count) {
  unsigned value = 0;  
  for (size_t index = 0; index < count; ++index) {
    unsigned power = count - index - 1;
    value += bits[index] << power;
  }
  return value;
}