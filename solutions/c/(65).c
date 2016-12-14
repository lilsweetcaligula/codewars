int basic_op(char op, int value1, int value2) {
  int result = 0;
  switch (op) {
    case '+':
      result = value1 + value2;
      break;
    case '-':
      result = value1 - value2;
      break;
    case '*':
      result = value1 * value2;
      break;
    case '/':
      result = value1 / value2;
      break;
    default:
      break;
  }
  return result;
}