/*
def diff_of_two(sequence, target = 2):
    sequence.sort()
    result = []
    first, last = 0, 1
    while last < len(sequence):
        difference = abs(sequence[first] - sequence[last])
        if difference == target:
            result.append([sequence[first], sequence[last]])
            first += 1
            last += 1
        elif difference < target:
            last += 1
        else:
            first += 1
    return result
*/

function twosDifference(sequence, target = 2) {
  sequence.sort((a, b) => a - b);
  let result = [];
  let first = 0, last = 1;
  while (last < sequence.length) {
    let difference = Math.abs(sequence[first] - sequence[last]);
    if (difference == target) {
      result.push([sequence[first], sequence[last]]);
      first += 1; last += 1;
    } else if (difference < target) {
      last += 1;
    } else {
      first += 1;
    }
  }
  return result;
}