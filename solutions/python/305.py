format_money = (lambda amount, sign = '$':
                     '{sign}{amount:.2f}'.format(sign = sign, amount = amount))