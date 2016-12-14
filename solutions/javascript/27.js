function isVow(a){
  for (let index in a) {
    let char = String.fromCharCode(a[index]);
    if ('aeiouAEIOU'.indexOf(char) >= 0) {
      a[index] = char;
    }
  }
  return a;
}function isVow(a){
  for (let index in a) {
    let char = String.fromCharCode(a[index]);
    if (/[aeiou]/i.test(char)) {
      a[index] = char
    }
  }
  return a;
}