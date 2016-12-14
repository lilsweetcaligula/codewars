#include <ctype.h>

char* swapCase(const char *string, char *buffer) {
  char c, *p = buffer;
	while (c = *string++) {
		*p++ = isupper(c) ? tolower(c) : toupper(c);
	}
	*p = '\0';
  return buffer;
}#include <ctype.h>

char* swapVowelCase(const char *string, char *buffer) {
  const static char *VOWELS = "aeouiAEOUI";
  char c, *p = buffer;
	while ((c = *string++) != '\0') {
		if (strchr(VOWELS, c)) {
			*p = isupper(c) ? tolower(c) : toupper(c);
		} else {
			*p = c;
		}
		++p;
	}
	*p = '\0';
  return buffer;
}