#include <stddef.h>
#include <string.h>
#include <stdio.h>

char *find_needle(const char **haystack, size_t count) {
  const char *needle = "needle";
  
  size_t index = 0;
  while (index < count && strcmp(haystack[index], needle) != 0) {
    ++index;
  }

  static const size_t BUFFER_LENGTH = 64;
  char *buffer = (char*)malloc(sizeof(char) * BUFFER_LENGTH);
  if (buffer) {
    if (index < count) {
      (void)snprintf(
        buffer, BUFFER_LENGTH, "found the needle at position %zd", index);
    } else {
      (void)snprintf(buffer, BUFFER_LENGTH, "needle not found");
    }
  }
  return buffer;
}