# coding=utf-8

import math


def check_right_angle(n):
    times = []
    for i in xrange(1, n/2):
        for j in xrange(1, n/2):
            max_num = max(i, j, n-i-j)
            min_num = min(i, j, n-i-j)
            left_num = math.pow(max_num, 2) - math.pow(min_num, 2)
            if check_sqrt(left_num) and check_same([n - i - j, i, j], [math.sqrt(left_num), max_num, min_num]):
                times.append([i, j, n-i-j])
    return count_list(times)


def check_same(m, n):
    m.sort()
    n.sort()
    return all(map(lambda x:x[0] == x[1], zip(m, n)))


def check_sqrt(n):
    return int(math.sqrt(n)) == math.sqrt(n)


def count_list(n):
    map(lambda x:x.sort(), n)
    times = []
    for i in n:
        if i not in times:
            times.append(i)
    return len(times)


def main():
    max_times = 0
    for i in xrange(1000):
        if check_right_angle(i) > max_times:
            max_num = i
            max_times = check_right_angle(i)
            print max_num, max_times
    return max_num, max_times


if __name__ == '__main__':
    print main()
    # print check_right_angle(120)
    # print check_right_angle(1000)
    # print check_same([1,2,3], [3,2,1])

# (840, 8)
