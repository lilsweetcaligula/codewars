def calculate(sentence):
    import re, operator
    pattern = r'(has|have).+?(?P<count>\d+).+\w*.+and.+(?P<action>lose[s]*|gain[s]*).(?P<change>\d+)'
    match = re.search(pattern, sentence)
    if match:
      count, change = int(match.group('count')), int(match.group('change'))
      action = None
      if match.group('action').startswith('gain'):
        action = operator.add
      elif match.group('action').startswith('lose'):
        action = operator.sub
      if action:
        return action(count, change)
    raise ValueError("Usage: <name> have|has <number> <items> and gain|gains|lose|loses <number>")