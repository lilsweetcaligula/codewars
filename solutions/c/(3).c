#include <ctype.h>
#include <stdio.h>

const char* position(char alphabet) {
  static char buffer[32];
  int pos = (isupper(alphabet) ? alphabet - 'A': alphabet - 'a') + 1;
  (void)snprintf(
    buffer, sizeof(buffer)/sizeof(buffer[0]), 
    "Position of alphabet: %d", pos);
  return buffer;
}