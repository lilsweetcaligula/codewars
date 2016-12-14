#include <stdlib.h>
#include <string.h>

char *stringLeftStrip(char *target, const char *chars) {
  size_t stripCount = strspn(target, chars ? chars : " ");
  return memmove(
    target, &target[stripCount], sizeof(char) * (strlen(target) + 1 - stripCount)) ? target : NULL;
}