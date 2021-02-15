# -*- coding: utf-8 -*-
import time
cache = {}


def local_cache(func):
    def inner(*args, **kwargs):
        key = "{}:{}".format(";".join(map(str, args)), ";".join(["{}:{}".format(*map(str, item)) for item in kwargs.items()]))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return inner


# 😂，在这里缓存无效，因为没有重复的计算量，反而会变得更慢
# @local_cache
def square_tile_num(hole=2, level=1):
    return sum([4*((hole+2*i)+1) for i in range(level)])


def calculate_upper(n=100):
    result = []
    # from one to ten level
    for i in range(1, 100):
        # from one hole to ten hole:
        for j in range(1, 100):
            if square_tile_num(j, i) <= n:
                result.append((j, i))
    return result


def big_calculate_upper(n=100):
    result = []
    i = 1
    while True:
        j = 1
        at_least_one = False
        while True:
            if square_tile_num(j, i) <= n:
                result.append((j, i))
                j += 1
                at_least_one = True
            else:
                break
        if at_least_one:
            i += 1
        else:
            break
    return result


if __name__ == '__main__':
    print(square_tile_num(2, 2))
    print(square_tile_num(7))
    print(square_tile_num(9, 1))
    start = time.time()
    print(calculate_upper(100))
    print(len(calculate_upper(100)))
    print(big_calculate_upper(100))
    print(len(big_calculate_upper(100)))
    print(time.time() - start)
    # print(cache)
    result = big_calculate_upper(1000000)
    # print(result)
    print(len(result))
    print(time.time() - start)
