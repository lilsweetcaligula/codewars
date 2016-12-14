function nthSmallest(/* ...arrays, n */) {
  // Good luck!
  
  // Thank you!
  return [].concat(
    ...Array.prototype
    .slice.apply(arguments, [0, arguments.length - 1]))
    .sort((a, b) => a - b)[arguments[arguments.length - 1] - 1];
}