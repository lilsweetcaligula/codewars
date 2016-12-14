#include <ctype.h>
#include <stddef.h>

int is_camelcase(const char *source) {
  const char *pchar;
  pchar = source;

  // Skip past whitespace.
  while (*pchar && isspace(*pchar)) ++pchar;

  if (*pchar && isalpha(*pchar) && islower(*pchar))
  {
  	// If reached the end of the string, the string may still be considered
  	// in camel case, however, the spec requires, we treat it as a string of
  	// unidentified format or "none".
  	//
  	// For this reason, traverse the source string until either a null-char
  	// is encountered or an uppercase one.
  	//
  	// If a null-char is encountered before the uppercase one, the string is
  	// to not be considered camelcase.
  	while (*pchar && (islower(*pchar) || isdigit(*pchar))) ++pchar;
  
  	if (*pchar)
  	{
  	  while (*pchar)
  	  {  
    		if (*pchar && isalpha(*pchar) && isupper(*pchar)) ++pchar;
    		else return 0;
    
    		if (*pchar && !islower(*pchar)) return 0;
    
    		while (*pchar && (islower(*pchar) || isdigit(*pchar))) ++pchar;
  	  }
  	  return 1;
  	}
  }
  return 0;
}

int is_snakecase(const char *source) { 
  static const char SEPARATOR = '_';
  const char *pchar;
  pchar = source;

  // Skip past whitespace.
  while (*pchar && isspace(*pchar)) ++pchar;

  if (*pchar)
  {
  	// If reached the end of the string, the string may still be considered
  	// in snake case, however, the spec requires, we treat it as a string of
  	// unidentified format or "none".
  	//
  	// For this reason, traverse the source string until either a null-char
  	// is encountered or a dash.
  	//
  	// If a null-char is encountered before a dash, the string is to not be
  	// considered camelcase.
  	while (*pchar && isalnum(*pchar)) ++pchar;
  
  	if (*pchar)
  	{
  	  while (*pchar)
  	  {
    		if (*pchar && *pchar == SEPARATOR) ++pchar;
    		else return 0;
    
    		if (*pchar && !islower(*pchar)) return 0;
    
    		while (*pchar && islower(*pchar)) ++pchar;
  	  }
  	  return 1;
  	}
  }
  return 0;
}

int is_kebabcase(const char *source) { 
  static const char SEPARATOR = '-';
  const char *pchar;
  pchar = source;

  // Skip past whitespace.
  while (*pchar && isspace(*pchar)) ++pchar;

  if (*pchar)
  {
  	// If reached the end of the string, the string may still be considered
  	// in kebab case, however, the spec requires, we treat it as a string of
  	// unidentified format or "none".
  	//
  	// For this reason, traverse the source string until either a null-char
  	// is encountered or an underscore.
  	//
  	// If a null-char is encountered before an underscore, the string is to 
  	// not be considered camelcase.
  	while (*pchar && isalnum(*pchar)) ++pchar;
  
  	if (*pchar)
  	{
  	  while (*pchar)
  	  {
    		if (*pchar && *pchar == SEPARATOR) ++pchar;
    		else return 0;
    
    		if (*pchar && !islower(*pchar)) return 0;
    
    		while (*pchar && islower(*pchar)) ++pchar;
  	  }
  	  return 1;
  	}
  }
  return 0;
}

typedef int(*StringMatcher)(const char*);

const char *case_id(const char *source) 
{
  static const StringMatcher MATCH_FUNCTIONS[] = { 
    is_camelcase, is_snakecase, is_kebabcase
  };
  
  static const char *RETURN_MESSAGES[] = {
    "camel", "snake", "kebab"
  };
  
  for (size_t index = 0; index < sizeof(MATCH_FUNCTIONS)/sizeof(MATCH_FUNCTIONS[0]); ++index) {
    if (MATCH_FUNCTIONS[index](source)) {
      return RETURN_MESSAGES[index];
    }
  }
  return "none";
}