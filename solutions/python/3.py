def delete_nth(order,max_e):
  counter = {}
  result = []
  for item in order:
    if item not in counter or item in counter and counter[item] < max_e:
      counter[item] = counter.get(item, 0) + 1
      result.append(item)
  return result