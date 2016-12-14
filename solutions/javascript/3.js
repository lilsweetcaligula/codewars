function voltage(arr,total,ndigits = 2) {
  const totalResistance = arr.reduce((a, b) => a + b);
  return arr.map(
    resistance => parseFloat((resistance / totalResistance * total).toFixed(ndigits)));
}