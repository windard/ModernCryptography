# coding=utf-8


def checkPalindromic(n):
    length = len(str(n))
    for i in xrange(int(length / 2)):
        if str(n)[i] != str(n)[length - i - 1]:
            return False
    return True


def checkLychrel(n):
    for i in xrange(50):
        # n *= 2
        n += int(str(n)[::-1])
        if checkPalindromic(n):
            return False
    return True

if __name__ == '__main__':
    # print checkPalindromic(1212243521)
    nums = []
    for i in xrange(1, 10000):
        if checkLychrel(i):
            nums.append(i)

    print len(nums)
    # print checkLychrel(196)
    # print checkLychrel(47)
    # print int(str(12324)[::-1])

# 249
