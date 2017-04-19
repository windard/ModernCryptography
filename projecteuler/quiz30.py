# coding=utf-8

# def division(n):
#     return n == sum([int(x)**len(str(n)) for x in str(n)])

# print sum([x for x in xrange(10000,100001) if division(x)])

import math


def divided(end):
    nums = []
    max_num = math.pow(9, end) * 10
    for i in xrange(2, int(max_num)):
        if sum(map(lambda x: math.pow(x, end), [int(j) for j in str(i)])) == i:
            nums.append(i)
    return nums

print sum(divided(5))
