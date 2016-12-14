#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int mxdiflg(
  const char **firstArray, size_t firstArrayLength, 
  const char **secondArray, size_t secondArrayLength) 
{
  if (firstArray && secondArray && firstArrayLength > 0 && secondArrayLength > 0) {
    int firstArrayMaxLength = 0;
    int firstArrayMinLength = 0;
    for (size_t index = 0; index < firstArrayLength; ++index) {
      const int length = (int)strlen(firstArray[index]);
	    if (index == 0) {
    		firstArrayMaxLength = length;
    		firstArrayMinLength = length;
  	  } else if (length > firstArrayMaxLength) {
        firstArrayMaxLength = length;
      } else if (length < firstArrayMinLength) {
        firstArrayMinLength = length;
      }
    }
    
    int secondArrayMaxLength = 0;
    int secondArrayMinLength = 0;
    for (size_t index = 0; index < secondArrayLength; ++index) {
      const int length = (int)strlen(secondArray[index]);
      if (index == 0) {
    		secondArrayMaxLength = length;
    		secondArrayMinLength = length;
  	  } else if (length > secondArrayMaxLength) {
        secondArrayMaxLength = length;
      } else if (length < secondArrayMinLength) {
        secondArrayMinLength = length;
      }
    }
    
    return (int)fmax(
      abs(firstArrayMaxLength - secondArrayMinLength), 
      abs(secondArrayMaxLength - firstArrayMinLength));
  }
  return -1;
}