#include <string.h>
#include <stdlib.h>

int calc(const char *source) {
  // I actually first saw this approach taken by code warriors
  // momoshangsang and daddepledge, and found it pretty neat.
  // Especially in C, where you save a kitten each time you 
  // manage not to have to allocate memory.

  size_t count = 0;
  
  // Count the number of 7's occuring in the ASCII code digits.
  const char *pchar;
  pchar = source;
  while (*pchar) {
    unsigned code = (unsigned)*pchar;
    while (code > 0) {
      if ((code % 10) == 7) {
        ++count;
      }
      code /= 10;
    }
    ++pchar;
  }
  
  return count * 6;
}