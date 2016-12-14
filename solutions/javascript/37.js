function last(x) {
  return x.split(" ")
    .sort(
      (a, b) => (a ? a[a.length - 1].charCodeAt(0) : 0) - (b ? b[b.length - 1].charCodeAt(0) : 0));
}