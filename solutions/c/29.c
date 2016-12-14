#include <stddef.h>
#include <ctype.h>

size_t find_longest(const char *words) {
  size_t length = 0, max_length = 0;
  const char *pchar = words;  
  while (1) {
    char c = *pchar++;
    if (!c || isspace(c)) {
      if (length > max_length) {
        max_length = length;
      }
      length = 0;
      if (!c) break;
    } else {
      length++;
    }
  }
  return max_length;
}