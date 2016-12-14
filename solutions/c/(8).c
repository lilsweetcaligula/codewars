#include <string.h>

int endsWith(const char *string, const char *suffix) {
	size_t stringLength = strlen(string);
	size_t suffixLength = strlen(suffix);
	if (suffixLength <= stringLength) {
		string += stringLength - suffixLength;
		while (*string && *suffix) {
			if (*string != *suffix) {
				return 0;
			}
			++string; ++suffix;
		}
		return 1;
	}
	return 0;
}