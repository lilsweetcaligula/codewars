#include <stdbool.h>
#include <ctype.h>

bool is_uppercase(const char *source) {
  if (*source) {
    return (!isalpha(*source) || isupper(*source)) && is_uppercase(&source[1]);
  }
  return true;
}