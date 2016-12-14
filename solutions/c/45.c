static unsigned countSetBitsHelper(const int value, const int currentBitCount);

unsigned countSetBits(const int value) {
  return countSetBitsHelper(value, 0);
}

unsigned countSetBitsHelper(const int value, const int currentBitCount) {
  if (value == 0) {
    return currentBitCount;
  }
  return countSetBitsHelper(value / 2, currentBitCount + value % 2);
}

const char *evil(int value) {
  return countSetBits(value) % 2 == 0 ? "It's Evil!" : "It's Odious!";
}