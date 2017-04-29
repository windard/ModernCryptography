# coding=utf-8

import math


def large_pow(n):
    large_n = 1
    for i in xrange(n):
        large_n *= n
        # print n,
        large_n = int(str(large_n)[-10:])
        # print n
    return large_n

allsum = 0
for i in xrange(1, 1001):
    # allsum += math.pow(i, i)
    allsum += large_pow(i)

print allsum

# 4629110846700
