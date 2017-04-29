# coding=utf-8

import fractions


# print fractions.Fraction.from_float(1.33333333333333)
# print fractions.Fraction.from_decimal('2/3')

nums = []

digitalSum = lambda n: reduce(lambda x, y: x+y, map(int, list(str(n))))

# def squareDivide(numerator, denominator, index):
#     if index > 10000:
#         return
#     global nums
#     denominator += 1 / 2.0
#     numerator = 1
#     data = 1 + numerator // denominator
#     numerator = fractions.Fraction.from_float(data).numerator
#     denominator = fractions.Fraction.from_float(data).denominator
#     squareDivide(numerator, denominator, index+1)


def squareDenominator(n):
    denominator = 0
    for i in xrange(n):
        denominator = 1.0 / (2.0 + denominator)

    return denominator


def squareDivide():
    for i in xrange(10):
        numerator = fractions.Fraction.from_decimal(fractions.Decimal(1.0 + squareDenominator(i))).numerator
        denominator = fractions.Fraction.from_decimal(fractions.Decimal(1.0 + squareDenominator(i))).denominator
        print numerator, denominator, 1.0 + squareDenominator(i)
        if digitalSum(numerator) > digitalSum(denominator):
            nums.append((numerator, denominator))

if __name__ == '__main__':
    squareDivide()
    print len(nums)
    # print fractions.Fraction('1 + 1/(2 + 1/(2 + 1/2))')
