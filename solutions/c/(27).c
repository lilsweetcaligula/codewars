int find_even_index(const int *values, int length) 
{  
  int sum = 0;
  for (int index = 0; index < length; index++) {
    sum += values[index];
  }  
  int left_sum = 0, right_sum = sum;
  for (int index = 0; index < length; index++) {
    left_sum += values[index];
    if (left_sum == right_sum) {
      return index;
    }
    right_sum -= values[index];
  }
  return -1;
}