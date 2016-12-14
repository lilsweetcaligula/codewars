#include <stdio.h>

int hex_to_dec(const char *source) {
  int value = 0;
  (void)sscanf(source, "%x", &value);
  return value;
}