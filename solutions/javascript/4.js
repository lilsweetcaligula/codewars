function abbrevName(name) {
  let names = name.split(" ");
  return names
    .map(name => name.slice(0, 1))
    .join(".");
}