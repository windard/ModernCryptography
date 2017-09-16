# coding=utf-8

def decomposeall(n):
    res = []
    for x in xrange(1,n):
        if n%x == 0:
            res.append(x)

    return res

def is_abundant(num):
    return sum(decomposeall(num)) > num

# for i in xrange(101):
#     if is_abundant(i):
#         print i,

sum_all = []

def check_abundant_sum(n):
    for i in xrange(n):
        for x in xrange(i/2 + 1):
            if is_abundant(x) and is_abundant(i-x):
                sum_all.append(i)
                break

check_abundant_sum(28123)
# print sum_all
# print set(xrange(28123)).difference(set(sum_all))
print sum(set(xrange(28123)).difference(set(sum_all)))
