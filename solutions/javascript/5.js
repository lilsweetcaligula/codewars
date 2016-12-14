function reverseByCenter(s){
  let mid = s.length / 2;
  return s.slice(-mid) + s.slice(mid, -mid) + s.slice(0, mid);
}