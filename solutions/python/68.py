def get_issuer(number):
  digits = str(number)
  issuers = {
      'AMEX': lambda digits: len(digits) == 15 and (digits.startswith('34') or digits.startswith('37')),
      'Discover': lambda digits: len(digits) == 16 and digits.startswith('6011'),
      'Mastercard': lambda digits: len(digits) == 16 and any(digits.startswith(str(prefix)) for prefix in range(51, 56)),
      'VISA': lambda digits: len(digits) in (13, 16) and digits.startswith('4')
  }
  for issuer, tester in issuers.items():
      if tester(digits):
          return issuer
  return 'Unknown'