#include <stdio.h>

int *split_odd_and_even(int value, size_t *pcount) 
{
  const size_t BUFFER_SIZE = sizeof(value) * 8 + 1;
  
  int *groups = (int*)malloc(sizeof(int) * BUFFER_SIZE);
  if (groups) 
  {  
  	char digits[BUFFER_SIZE];
  
  	(void)snprintf(digits, BUFFER_SIZE, "%d", value);
    
  	const char *slow, *fast;
  	slow = digits;
  	fast = &digits[1];
    
  	*pcount = 0;
  	groups[*pcount] = *digits - '0';
  	int parity = *digits % 2;
    
  	while (*fast) 
  	{
  	  int new_parity = *fast % 2;
      
  	  if (new_parity != parity) {
  		groups[++*pcount] = 0;
  		parity = new_parity;
  	  }
  	  groups[*pcount] = groups[*pcount] * 10 + *fast - '0';
      
  	  ++slow; ++fast;
  	}
  	++*pcount;
  }
  return groups;
}