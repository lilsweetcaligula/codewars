function realSize(arrays) {
  return arrays.reduce(function (previousValue, currentValue) {
    return previousValue + (currentValue instanceof Array ? realSize(currentValue) : 1);
  }, 0);
}