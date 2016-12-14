function isIntArray(arr) {
  return Boolean(arr) && arr.length === arr.filter(
    value => typeof(value) === "number" && Math.floor(value) == value).length;
}