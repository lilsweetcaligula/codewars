def calculate_years(principal, interestRate, taxRate, desiredSum):
  yearCount = 0
  while principal < desiredSum:
    principal = principal + principal * interestRate - principal * interestRate * taxRate
    yearCount += 1
  return yearCount
