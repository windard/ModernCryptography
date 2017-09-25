# coding=utf-8

import math


def check_prime(n):
    if n in (0, 1):
        return False
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def prime():
    yield 2
    start = 3
    while 1:
        if check_prime(start):
            yield start
        start += 2


def all_circule(n):
    m = [int(i) for i in str(n)]
    circules = []
    while True:
        if tuple(m) in circules:
            break
        circules.append(tuple(m))
        m.append(m.pop(0))
    return circules


def solve(n):
    p = prime()
    f = p.next()
    nums = []
    while True:
        if f > n:
            break
        circules = all_circule(f)
        if all(map(lambda x: check_prime(int(''.join(map(str, x)))), circules)):
            nums.append(f)
        f = p.next()
    return nums


if __name__ == '__main__':
    # print all_circule(3)
    # print all_circule(5)
    # print all_circule(34)
    # print all_circule(897)
    # print len(solve(100))
    print len(solve(1000000))
    # print sum(solve(1000000))
