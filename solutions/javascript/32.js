function dropWhile(arr, pred) {
  let start = arr.findIndex((a) => !pred(a));
  return start >= 0 ? arr.slice(start) : [];
}