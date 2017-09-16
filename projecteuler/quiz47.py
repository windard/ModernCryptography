# coding=utf-8

import math


def decompose(n):
    i = 1
    res = []
    while i < math.sqrt(n):
        i += 1
        if n % i == 0:
            n = n / i
            res.append(i)
            i = 1
    res.append(int(n))
    return res


# def main(a, b, size):
#     for i in xrange(a, b):
#         if len(set(decompose(i))) == size and len(set(decompose(i + 1))) == size:
#             # return i
#             print i
#     # return None

def main(size):
    i = 1
    while i:
    # for i in xrange(10000):
        if check_size(i, size):
            return i
        i += 1



def check_size(n, size):
    for i in xrange(n, n+size):
        if len(set(decompose(i))) != size:
            return False
    return True


if __name__ == '__main__':
    print main(4)
    # print main(10, 99, 2)
    # print main(100, 999, 3)
    # main(1000, 9999, 4)
    # for i in xrange(1000, 9999):
        # if len(set(decompose(i))) == 4:
            # print i, set(decompose(i))
    # print set(decompose(4563))
    # print decompose(644)

# 7314
# 8294
# 8645
# 9009


# 134043
