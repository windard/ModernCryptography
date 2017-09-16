# coding=utf-8

import math

def check_prime(n):
    if n in (0, 1):
        return False
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solve(n):
    nums = []
    for i in xrange(10, n):
        if not check_prime(i):
            continue
        for j in xrange(1, len(str(i))):
            if not check_prime(int(str(i)[j:])):
                break
            if not check_prime(int(str(i)[:-j])):
                break
        else:
            nums.append(i)
    return nums

if __name__ == '__main__':
    print sum(solve(1000000))

# 23
# 37
# 53
# 73
# 313
# 317
# 373
# 797
# 3137
# 3797
# 739397
