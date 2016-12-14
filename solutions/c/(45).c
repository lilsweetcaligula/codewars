#include <string.h>

char* reverser(char *sentence) {
  static const char *DELIMITERS = " ";
  char *pStart = sentence;
  char *pEnd = sentence;
  while (*pEnd) {
    while (*pEnd && !strchr(DELIMITERS, *pEnd)) {
      ++pEnd;
    }
    char *pSubStart = pStart;
    char *pSubEnd = pEnd - 1;
    while (pSubStart < pSubEnd) {
      char temp = *pSubStart;
      *pSubStart = *pSubEnd;
      *pSubEnd = temp;
      ++pSubStart; --pSubEnd;
    }
    while (*pEnd && strchr(DELIMITERS, *pEnd)) {
      ++pEnd;
    }
    pStart = pEnd;
  }
  return sentence;
}