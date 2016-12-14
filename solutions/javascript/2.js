function moveTen(s, count = 10) {
  return s.split("")
    .map(char => (char.charCodeAt(0) + count - (/[A-Z]/.test(char) ? 'A'.charCodeAt(0) : 'a'.charCodeAt(0))) 
        % 26 + (/[A-Z]/.test(char) ? 'A'.charCodeAt(0) : 'a'.charCodeAt(0)))
    .map(charCode => String.fromCharCode(charCode)).join("");
}