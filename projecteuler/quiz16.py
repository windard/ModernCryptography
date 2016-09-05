# coding=utf-8

import math

def countsum(n):
	res = 0
	# digitalsum = math.pow(2,n)
	digitalsum = 2**n
	for x in str(int(digitalsum)):
		res += int(x)

	return res

print countsum(1000)