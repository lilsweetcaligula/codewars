def to_cents(amount):
  import re
  match = re.match(r'\A\$(\d+)\.(\d{2})\Z', amount)
  return int(match.expand(r'\1\2')) if match else Nonedef to_cents(amount):
    import re
    match = re.match(r'\A\$(?P<dollars>\d+)\.(?P<cents>\d{2})\Z', amount)
    return(
        int(match.group('dollars')) * 100 + int(match.group('cents')) if match 
        else None)