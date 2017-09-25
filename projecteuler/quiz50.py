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


def check_consecutive(n):
    p = prime()
    f = p.next()
    m = []
    while f < n:
        if sum(m) < n:
            m.append(f)
            f = p.next()
        elif sum(m) > n:
            m.pop(0)
        else:
            return m

def solve(n):
    p = prime()
    f = p.next()
    nums = []
    while f < n:
        cur = check_consecutive(f)
        if cur:
            nums.append(cur)
        f = p.next()
    return nums

if __name__ == '__main__':
    # print check_consecutive(59)
    # print check_consecutive(953)
    # print check_consecutive(2)
    # print check_consecutive(5)
    # print check_consecutive(11)
    # print check_consecutive(13)
    # print check_consecutive(17)
    # print check_consecutive(23)
    # print check_consecutive(29)
    # print check_consecutive(31)
    # nums = solve(1000000)
    # nums = solve(1000000)
    nums = solve(1000000)
    print nums
    sort_nums = {len(i):sum(i) for i in nums}
    # print sort_nums
    print sorted(sort_nums.iteritems(),key=lambda a:a[0],reverse=True)

    # 997651

