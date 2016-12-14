#include <math.h>
#include <string.h>

static double add(const double a, const double b) {
  return a + b;
}

static double div(const double a, const double b) {
  return a / b;
}

static double sub(const double a, const double b) {
  return a - b;
}

static double mul(const double a, const double b) {
  return a * b;
}

typedef double (*mathOperation)(const double a, const double b);

double arithmetic(double a, double b, char* operator) {
  const mathOperation OPERATIONS[] = { 
    &add, &div, &sub, &mul
  };
  const char *OPERATORS[] = {
    "add", "divide", "subtract", "multiply"
  };
  for (size_t index = 0; index < sizeof(OPERATORS)/sizeof(OPERATORS[0]); ++index) {
    if (!strcmp(operator, OPERATORS[index])) {
      return (*OPERATIONS[index])(a, b);
    }
  }
  return INFINITY;
}