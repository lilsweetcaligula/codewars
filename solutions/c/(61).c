#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *borrow(const char *source) {
  char *buffer = (char*)malloc(sizeof(char) * (strlen(source) + 1));
  if (buffer) 
  {
    const char *psource = source;
    char *pbuffer = buffer;
    
    char c;
    while ((c = tolower(*psource++))) {
      if (c >= 'a' && c <= 'z') {
        *pbuffer++ = c;
      }
    }
    *pbuffer = '\0';
  }
  return buffer;
}