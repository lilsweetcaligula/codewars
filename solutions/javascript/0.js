// complete the function
function solution(s) {
  let firstRegexp = /^[a-z]+(?=[A-Z])/;
  let secondRegexp = /[A-Z][a-z]+?(?=[A-Z]|$)/g;
  
  let result = firstRegexp.exec(s);  
  let next = [];
  while (next) {
    result = result.concat(next);
    next = secondRegexp.exec(s);
  }  
  return result.join(" ");
}
