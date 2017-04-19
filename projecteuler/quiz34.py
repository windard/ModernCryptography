# coding=utf-8

import math


def cala():
    nums = []
    max_num = math.factorial(9) * 10
    for i in xrange(3, max_num):
        if sum(map(lambda x: math.factorial(x), [int(j) for j in str(i)])) == i:
            nums.append(i)
    return nums

print sum(cala())
