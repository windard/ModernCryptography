# coding=utf-8

Pentagonal = lambda x: x * (3 * x - 1) / 2

nums = map(Pentagonal, xrange(1, 10000))

# print nums

pairs = []

import itertools

for item in itertools.combinations(nums, 2):
    if sum(item) in nums and abs(item[0] - item[1]) in nums:
        pairs.append(abs(item[0] - item[1]))

print min(pairs)


# 5482660
