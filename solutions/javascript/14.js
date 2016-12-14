function twoSort(s, rcount = 3) {
  s.sort();
  return s.join() && s[0].split('').join('*'.repeat(rcount));
}function twoSort(s, rcount = 3) {
  s.sort();
  let chars = s && s[0].split('');
  let result = '';
  for (let index in chars) {
    result += chars[index] + (index == chars.length - 1 ? '' : '*'.repeat(rcount));
  }
  return result;
}