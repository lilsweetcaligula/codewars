#include <stddef.h> // size_t

long long thirt(long long n)
{
  const long long remainders[] = { 1, 10, 9, 12, 3, 4 };
  
  long long value = n;
  long long currSum = 0;
  long long prevSum = 0;

  do {
    size_t remIndex = 0;

  	prevSum = currSum;
  	currSum = 0;
    
    while (value > 0) 
    {
      const long long rem = remainders[remIndex];
      const long long dig = value % 10;
      currSum += dig * rem;
      
      remIndex = (remIndex + 1) % (sizeof(remainders)/sizeof(remainders[0]));
      value /= 10;
    }
    value = currSum;
  } while (currSum != prevSum);

  return value;
}