function meanVsMedian(numbers) {
  if (!numbers || numbers.length == 0) {
    return undefined;
  }
  let median = numbers.sort((a, b) => a - b)[Math.floor(numbers.length / 2)];
  let mean = numbers.reduce((a, b) => a + b) / numbers.length;
  if (median == mean) return 'same';
  return median > mean ? 'median' : 'mean';
}