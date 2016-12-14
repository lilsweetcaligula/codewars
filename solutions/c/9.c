int startsWith(const char *string, const char *prefix) {
	while (*string && *prefix) {
		if (*string != *prefix) {
			return 0;
		}
		++string; ++prefix;
	}
	return !*prefix;
}#include <string.h>

int startsWith(const char *string, const char *prefix) {
  return strstr(string, prefix) == string;
}