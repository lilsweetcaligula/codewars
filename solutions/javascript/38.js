function leaderB(user, user_score, your_score) {
  const BETA_SCORE = 3;
  const DEFAULT_SCORE = 1;
  let difference = user_score - your_score;
  if (difference > 0) {
    let beta_count = Math.floor(difference / BETA_SCORE);
    let default_count = Math.floor((difference - beta_count * BETA_SCORE) / DEFAULT_SCORE);
    return 'To beat ' + user + '\'s score, I must complete ' + beta_count 
      + ' Beta kata and ' + default_count + ' 8kyu kata.' 
      + (beta_count + default_count > 1000 ? ' Dammit!' : '');
  }
  else if (difference == 0) {
    return 'Only need one!';
  }
  return 'Winning!';
}