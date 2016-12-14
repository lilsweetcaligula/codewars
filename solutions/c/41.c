#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *accum(const char *source) {
  static const char SEPARATOR[] = "-";
  
  // Cannot use strlen(SEPARATOR) if we want to place SEPARATOR_LENGTH in
  // the static memory. - Not a compile time constant.
  static const size_t SEPARATOR_LENGTH = sizeof(SEPARATOR)/sizeof(SEPARATOR[0]) - 1;

  const size_t sourceLength = strlen(source);
  
  // See: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
  // sum(range(n + 1)) == n * (n + 1) / 2
  // + length(separator) * (length(source) - 1) == the number of the separator chars.
  const size_t resultLength = sourceLength * (sourceLength + 1) / 2 +
    SEPARATOR_LENGTH * (sourceLength - 1);

  char *buffer = (char*)malloc(sizeof(char) * (resultLength + 1));
  if (buffer) 
  {
    char *pdest = buffer;
    for (size_t index = 0; index < sourceLength; ++index) 
    {
      const char currLetter = source[index];
      const size_t repeatCount = index + 1;
      
      for (size_t times = 0; times < repeatCount; ++times) {
        if (times == 0) {
          *pdest = toupper(currLetter);
        } else {
          *pdest = tolower(currLetter);
        }
        ++pdest;
      }
      
      if (index != sourceLength - 1) {
        (void)strcpy(pdest, SEPARATOR);
        pdest += SEPARATOR_LENGTH;
      }      
    }
    *pdest = '\0';
  }
  return buffer;
}