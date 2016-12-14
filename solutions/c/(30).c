#include <stddef.h> // NULL
#include <ctype.h>

char *to_alternating_case(char *string) {
  static size_t length;
  
  if (!*string) {
    length = 0;
  }
  else {
    ++length;
    
    string[0] = isupper(string[0]) ? tolower(string[0]) : toupper(string[0]);
    (void)to_alternating_case(&string[1]);
  }
  
  return string - length;
}