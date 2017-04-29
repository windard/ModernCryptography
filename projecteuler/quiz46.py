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


def checkTrue(a):
    for i in prime(a):
        item = math.sqrt((a - i) / 2)
        # print i, item
        if item == math.floor(item):
            return True
    return False

if __name__ == '__main__':
    # for i in xrange(7, 21, 2):
        # if checkTrue(i):
            # print i,
    # print checkTrue(25)
    start = 9
    while 1:
        if not checkTrue(start):
            print start
            break

        start += 2

    # print math.sqrt(10)
    # print math.floor(math.sqrt(10))
    # print math.sqrt(10) == math.floor(math.sqrt(10))

    # print checkPrime(2)

    # print len(filter(checkPrime, xrange(2, 1014)))
    # print [i for i in xrange(2, 10) if checkPrime(i)]

    # print checkPrime(6)
    # print len(list(prime(1014)))
    # a = prime(10)
    # print a.next()
    # print a.next()
    # print a.next()
    # print a.next()
    # print a.next()

    # print list(prime(10))
    # for i in prime(10):
    #     print i,

# 5777
