# coding=utf-8

import math


def checkPrime(a):
    for i in xrange(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True


def prime(a):
    yield 2
    start = 3
    while 1:
        if start > a:
            break
        if checkPrime(start):
            yield start
        start += 2


def prime_group(a, b):
    for i in xrange(a, b):
        if checkPrime(i):
            yield i

# for i in prime_group(100, 200):
# print list(prime_group(10, 100))
# print len(list(prime_group(10, 100)))

# print list(str(1999))
# for i in prime_group(1000, 9999):
import itertools

# for item in itertools.combinations(prime_group, 3):
#     if list(item[0]) == list(item[1]) == list(item[2]):
#         print item

# print list(str(1999))
# print list(str(9199))
# print list(str(1999)) == list(str(9199))


class MyList(list):

    def __eq__(self, *args, **kwargs):
        # print args, kwargs
        for i in self:
            if i not in args[0]:
                return False
            if self.count(i) != args[0].count(i):
                return False
        else:
            if len(self) == len(args[0]):
                return True
            return False

for item in itertools.combinations(prime_group(1000, 9999), 3):
    if MyList(str(item[0])) == MyList(str(item[1])) == MyList(str(item[2])):
        # print item
        item = list(item)
        maxnum = max(item)
        minnum = min(item)
        item.remove(maxnum)
        item.remove(minnum)
        leftnum = item.pop()
        if maxnum - leftnum == leftnum - minnum:
            print minnum, leftnum, maxnum

# print MyList(str(1999))
# print MyList(str(9199))
# print MyList(str(1009)) == MyList(str(1019)) == MyList(str(1091))

# item = [1487, 4817, 8147]

# maxnum = max(item)
# minnum = min(item)
# item.remove(maxnum)
# item.remove(minnum)
# leftnum = item.pop()
# print leftnum, maxnum, minnum

# a = tuple([1, 2, 3])
# b = list(a)

# print type(a), type(b)
# print a, b

# 1487 4817 8147
# 2969 6299 9629
