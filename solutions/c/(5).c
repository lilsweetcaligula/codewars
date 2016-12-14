#include <string.h>

char* replaceNth(const char* text, int n, char oldValue, char newValue) {
  size_t textLength = strlen(text);
  char *buffer = (char*)malloc((textLength + 1) * sizeof(char));
  if (buffer) {
    for (size_t index = 0, times = 0; index < textLength; ++index) {
      if (text[index] == oldValue) {
        ++times;
      }
      if (text[index] == oldValue && times == n) {
        buffer[index] = newValue;
        times = 0;
      } else {
        buffer[index] = text[index];
      }
    }
    buffer[textLength] = '\0';
  }
  return buffer;
}