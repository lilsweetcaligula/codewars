int* seven(long long m) {
    static int ret[2] = { 0 };

    long long value = m;
    int count = 0;

    while (value % 100 < value) 
    {    
	    // Stop when the number is at most 2 digits.

	    const long long x = value / 10;
      const long long y = value % 10;        
      value = x - 2 * y;

      ++count;
    }

    ret[0] = (int)value;
    ret[1] = count;
    return ret;
}