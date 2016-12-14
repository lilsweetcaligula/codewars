#include <string.h>

int correct_tail(const char *body, const char *tail) {
  size_t tail_length = strlen(tail);
  size_t body_length = strlen(body);
  if (tail_length <= body_length) {
    size_t offset = body_length - tail_length;
    const char *pchar = &body[offset];
    while (*pchar && *tail) {
      if (*pchar != *tail) {
        return 0;
      }
      pchar++; tail++;
    }
    return 1;
  }
  return 0;
}