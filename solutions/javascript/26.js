function facRecursion(value){
  return value < 0     ? 
         0 : value < 2 ? 
         1 : value * facRecursion(value - 1);
}