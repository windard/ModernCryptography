# -*- coding: utf-8 -*-


def _is_bouncy(n):
    if n < 10:
        return False
    times = 0
    last = int(str(n)[0])
    for i in map(int, list(str(n))[1:]):
        if i > last:
            times += 1
        elif i < last:
            times -= 1
        last = i

    print(times)
    return not bool(times)


def is_bouncy(n):
    # 即不是递增，也不是递减，就是 bouncy 数

    flag = 0
    last = None
    for i in map(int, list(str(n))):
        if last is None:
            last = i
            continue
        if i > last:
            new_flag = 1
        elif i < last:
            new_flag = -1
        else:
            last = i
            continue

        if flag != 0 and new_flag != flag:
            return True
        flag = new_flag

        last = i

    return False


def bette_is_bouncy(n):
    dec = False
    inc = False

    n, last = divmod(n, 10)

    while n:
        n, i = divmod(n, 10)
        if i < last:
            dec = True
        elif i > last:
            inc = True
        last = i

        if dec and inc:
            return True

    return False


def find_bouncy_num(n):
    i = 0
    count = 0
    while i < n:
        i += 1
        if bette_is_bouncy(i):
            count += 1

    return count


def find_bouncy_frequency(frequency):
    i = 0
    count = 0
    while True:
        i += 1
        if bette_is_bouncy(i):
            count += 1

        if float(count) / float(i) == frequency:
            return i


if __name__ == '__main__':
    # print(is_bouncy(134468))
    # print(is_bouncy(66420))
    # print(is_bouncy(155349))
    # print(find_bouncy_num(1000))
    # print(find_bouncy_frequency(0.5))
    # print(find_bouncy_frequency(0.9))
    # print(find_bouncy_frequency(0.99))
    print(bette_is_bouncy(134468))
    print(bette_is_bouncy(66420))
    print(bette_is_bouncy(155349))
    print(find_bouncy_num(1000))
    print(find_bouncy_frequency(0.5))
    print(find_bouncy_frequency(0.9))
    print(find_bouncy_frequency(0.99))
