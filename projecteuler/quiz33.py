# coding=utf-8

from __future__ import division

# def check_trivial(numerator, denominator):
#     source =  numerator / denominator
#     for i in xrange(len(str(numerator))):
#         n = int(str(numerator)[i])
#         for j in xrange(len(str(denominator))):
#             d = int(str(denominator)[j])
#             try:
#                 if source == n / d:
#                     return True
#             except ZeroDivisionError:
#                 pass
#     return False

# print check_trivial(49, 98)
# print check_trivial(15, 56)
# print check_trivial(30, 50)

def check_trivial(numerator, denominator):
    if numerator >= denominator:
        return False
    source =  numerator / denominator
    same = set(str(numerator)) & (set(str(denominator)))
    numerator = set(str(numerator)) - same
    denominator = set(str(denominator)) - same
    if not numerator or not denominator:
        return False
    try:
        if len(same) == 1 and same.pop() != str(0) and source == int(numerator.pop()) / int(denominator.pop()):
            return True
    except ZeroDivisionError:
        return False
    return False


def solve(n):
    nums = []
    for i in xrange(10, n):
        for j in xrange(10, n):
            if check_trivial(i, j):
                nums.append((i, j))
    return nums


def main():
    for y in range(1, 10):
        for z in range(9, y, -1):
            x,rest = divmod(9 * y * z, 10 * y - z)
            if rest == 0 and x < 10:
                print("{}/{}={}/{}".format(10 * y + x, z + 10 * x, y, z))


if __name__ == '__main__':
    print solve(100)
    # print check_trivial(49, 98)
    # print check_trivial(30, 90)
    # print check_trivial(23, 45)
    # print check_trivial(23, 45)
    # print check_trivial(23, 15)
    print check_trivial(23, 45)