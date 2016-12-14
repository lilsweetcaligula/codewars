function flatten() {
  let values = Array.prototype.slice.call(arguments);
  let result = [];
  for (let value of values) {
    if (value instanceof Array) {
      result = result.concat(flatten.apply(null, value));
    } else {
      result.push(value);
    }
  }
  return result;
}