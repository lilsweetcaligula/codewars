#include <stdlib.h>
#include <stdio.h>

char *switcher(const char **codes, size_t count) {
  char *result = (char*)malloc(sizeof(char) * (count + 1));
  if (result) {
    char *pchar = result;
    for (size_t index = 0; index < count; ++index) {
      int value = 0;
      (void)sscanf(codes[index], "%d", &value);

      char ch;
      switch (value) {
        case 27:
          ch = '!';
          break;
        case 28:
          ch = '?';
          break;
        case 29:
          ch = ' ';
          break;
        default:
          ch = (char)('z' + 1 - value);
          break;
      }
      
      *pchar++ = ch;
    }
    *pchar = '\0';
  }
  return result;
}