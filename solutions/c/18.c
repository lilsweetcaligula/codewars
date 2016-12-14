#include <stddef.h>

struct IntegerPair {
  int key;
  int value;
};

int gcd(int n, int m) {
  while (m > 0) {
    int temp = m;
    m = n % m;
    n = temp;
  }
  return n;
}

int lcm(int n, int m) {
  if (m == 0) {
    return 0;
  }
  return (n * m) / gcd(n, m);
}

int sum_differences_between_products_and_LCMs(struct IntegerPair *pairs, size_t count) {
  int result = 0;
  for (size_t index = 0; index < count; ++index) {
    int product = pairs[index].key * pairs[index].value;
    int last_common_multiple = lcm(pairs[index].key, pairs[index].value);
    result += product - last_common_multiple;
  }
  return result;
}