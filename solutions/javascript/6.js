function arr2bin(arr) {
  arr = arr.map((a) => !Number.isNaN(a) && !Number.isFinite(a) ? 0 : a)
  return( 
    (arr && arr.length > 0) ?
      arr.reduce((a, b) => a + b).toString(2) : '0');
}