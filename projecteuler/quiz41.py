# coding=utf-8

import math
import itertools

def checkPrime(n):
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def main():
    n = ''
    for i in xrange(1, 10):
        n += str(i)
        for item in itertools.permutations(n, i):
            num = int(''.join(item))
            if checkPrime(num):
                print '*', num

if __name__ == '__main__':
    main()

# 7652413
