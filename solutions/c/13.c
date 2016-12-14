int mod256WithoutMod(int number)
{
  static const MOD_VALUE = 256;
  return number - number / MOD_VALUE * MOD_VALUE;
}