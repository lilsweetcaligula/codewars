void fakeBin(const char *digits, char *buffer) {
  // Please place result in the memory pointed to by
  // the buffer parameter. Buffer has enough memory to
  // accommodate the answer as well as the null-terminating
  // character.

  char digit, *pchar = buffer;
  while ((digit = *digits++)) *pchar++ = digit - '0' < 5 ? '0' : '1';
  *pchar = '\0';
}