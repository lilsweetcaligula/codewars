function fakeBin(digits) {
  return digits
    .split("")
    .map(value => parseInt(value))
    .map(value => value < 5 ? '0' : '1')
    .join("");
}