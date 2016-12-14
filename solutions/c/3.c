#include <stdarg.h>
#include <stdio.h>

char* formatString(char *buffer, size_t bufferLength, const char *format, ...) {
  va_list vargs;
  va_start(vargs, format);
  vsnprintf(buffer, bufferLength, format, vargs);
  va_end(vargs);
  return buffer;
}