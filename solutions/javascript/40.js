Array.prototype.average = function() {
  return this.length && this.reduce((a, b) =>
    (a instanceof Array ? a.average() : parseFloat(a)) + (b instanceof Array ? b.average() : parseFloat(b))
  ) / this.length;
}Array.prototype.average = function() {
  return this
    .slice()
    .reduce((a, b) => 
      (a instanceof Array ? a.average() : parseFloat(a)) + 
      (b instanceof Array ? b.average() : parseFloat(b))) 
    / this.length;
}