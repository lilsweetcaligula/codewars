function span(arr, pred) {
  let pivot = arr.findIndex((a) => !pred(a));
  pivot = pivot >= 0 ? pivot : arr.length;
  return [arr.slice(0, pivot), arr.slice(pivot, arr.length)];
}