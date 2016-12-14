#include <string.h>

const char* greet(const char *name, const char *owner) {
  return strcmp(name, owner) == 0 ? "Hello boss" : "Hello guest";
}