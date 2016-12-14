#include <string.h>

char* my_strtok(char *src, const char *delims) {
  static char *currtok, *tokend;

  if (src) {
    currtok = src;
    while (*src) {
      if (strchr(delims, *src)) {
        *src = '\0';
      }
      ++src;
    }
    tokend = src;
  } else {
    while (currtok != tokend && *currtok) {
      ++currtok;
    }    
  }

  while (currtok != tokend && !*currtok) {
    ++currtok;
  }
  if (currtok == tokend) {
    currtok = NULL;
  }
  return currtok;
}