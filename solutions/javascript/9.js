function secondLargest(array) {
  if (!array || !(array instanceof Array)) {
    return undefined;
  }
	array = array
		.sort	  ((a, b) => b - a)
		.filter	((a) => Number.isFinite(parseInt(a)))
		.map    ((a) => parseInt(a));
  let index = 1;
  while (index < array.length && array[index - 1] == array[index]) {
    ++index;
  }
  return array[index];
}