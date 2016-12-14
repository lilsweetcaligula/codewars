char* filterRefsOut(char *source) {
  char *slow, *fast;
  slow = source;
  fast = source;
  while (*slow) {
    if (*fast == '[') {
      while (*fast) {
        if (*fast == ']') {
          ++fast;
          break;
        }
        ++fast;
      }
    } else {
      *slow = *fast;
      ++slow; ++fast;
    }
  }
  return source;
}char* filterRefsOut(char *source) {
  char *slow, *fast;
  slow = source;
  fast = source;
  while (*slow) {
    if (*fast == '[') {
      while (*fast) {
        if (*fast == ']') {
          ++fast;
          break;
        }
        ++fast;
      }
    } else {
      *slow = *fast;
      ++slow; ++fast;
    }
  }
  return source;
}