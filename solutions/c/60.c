#include <string.h>

char *repeat_str(size_t count, const char *src) {
  size_t srcLength = strlen(src);
  char *result = (char*)calloc(1 + count * srcLength, sizeof(char));
  if (result) {
    for (size_t times = 0, index = 0; times < count; ++times, index += srcLength) {
      (void)strcpy(&result[index], src);
    }
  }
  return result;
}