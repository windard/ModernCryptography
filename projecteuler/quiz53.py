# coding=utf-8

import math


def Colm(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# mul = 1
# for i in xrange(10, 24):
#     mul *= i

# print mul

# print Colm(23, 10)

# print math.factorial(0)

pairs = []

for i in xrange(1, 101):
    for j in xrange(i+1):
        if Colm(i, j) >= 1000000:
            pairs.append((i, j))

print len(pairs)

# factorial
