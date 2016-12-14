#include <ctype.h>

int get_number_from_string(const char *src) {
  int value = 0;  
  char c;
  while ((c = *src++)) if (isdigit(c)) value = value * 10 + (c - '0');
  return value;
}