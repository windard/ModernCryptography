# coding=utf-8

import math

def calc(end):
	nums = []
	for x in xrange(2, end+1):
		for y in xrange(2, end+1):
			nums.append(math.pow(x, y))
	# print sorted(set(nums))
	return len(set(nums))

print calc(100)