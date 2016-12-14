#include <stdlib.h>

const char* how_much_i_love_you(int nb_petals) {
  const char *OPTIONS[] = {
    "I love you", "a little", "a lot",
    "passionately", "madly", "not at all",
  };
  const int OPTIONS_SIZE = (int)(sizeof(OPTIONS) / sizeof(OPTIONS[0]));
  return OPTIONS[(nb_petals - 1) % OPTIONS_SIZE];
}