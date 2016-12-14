var f = (n) => Boolean(
  typeof n === 'number' && Math.floor(n) === n && n > 0
) && (n * (n + 1)) / 2