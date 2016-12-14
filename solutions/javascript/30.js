function borrow(s){
  return s.split("")
    .filter(char => /[A-Za-z]/.test(char))
    .map(char => char.toLowerCase()).join("");
}