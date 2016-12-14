#include <ctype.h>

char *to_alternating_case(char *string) {
  char ch, *pChar;  
  pChar = string;
  while ((ch = *pChar) != '\0') {
    *pChar = isupper(ch) ? tolower(ch) : toupper(ch);
    ++pChar;
  }
  return string;
}