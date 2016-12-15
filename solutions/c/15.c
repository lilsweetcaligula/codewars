#include <stddef.h>

unsigned binary_array_to_numbers(const unsigned *bits, size_t count) {
  unsigned value = 0;  
  unsigned power = count - 1;
  for (size_t index = 0; index < count; ++index) {
    value += bits[index] << power;
    --power;
  }
  return value;
}
