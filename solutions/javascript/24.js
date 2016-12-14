function collatz(n, count) {
  if (n == 1) return count ? count : 1;
  return collatz(n % 2 ? 3 * n + 1 : n / 2, count ? count + 1 : 2);
}