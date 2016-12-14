function dropWhile(arr, pred) {
  return arr.slice(
    (arr.findIndex((a) => !pred(a)) + 1 || arr.length + 1) - 1, arr.length);
}