def reduce(fraction):
    from fractions import Fraction
    f = Fraction(*fraction)
    return [f.numerator, f.denominator]def reduce(numeratorAndDenominator):
    from fractions import Fraction
    numerator, denominator = numeratorAndDenominator
    fraction = Fraction(numerator, denominator)
    return [fraction.numerator, fraction.denominator]