char* isSortedAndHow(int* array, int arrayLength) {
  if (arrayLength > 1) {
    int direction = array[1] - array[0];
    for (int index = 1; index < arrayLength; ++index) {
      if (
        (direction > 0 && array[index] - array[index - 1] < 0) ||
        (direction < 0 && array[index] - array[index - 1] > 0)) 
      {
        return "no";
      }
    }
    return direction < 0 ? "yes, descending" : "yes, ascending";
  }
  return arrayLength == 1 ? "yes, ascending" : "no";
}