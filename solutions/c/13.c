int mod256WithoutMod(int number)
{
  /* December 15, 2016
   * lilsweetcaligula: this code can be further simplified with
   * a little knowledge of binary math:
   * 
   * const int ret = number & 0xFF;
   */
  static const MOD_VALUE = 256;
  return number - number / MOD_VALUE * MOD_VALUE;
}
