function switcher(codes) {
  const extra = {
    27: '!', 28: '?', 29: ' '
  };
  return codes
    .map(code => code in extra ? extra[code] : String.fromCharCode("a".charCodeAt(0) + 26 - code))
    .join("");
}