function filterHomogenous(arrays) {
	return arrays && arrays.filter(array =>
    array.length > 0 && array.every(value => typeof(array[0]) === typeof(value)));
}