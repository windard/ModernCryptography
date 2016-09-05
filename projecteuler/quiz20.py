# coding=utf-8

import math

def countdigital(n):
	facnum = math.factorial(n)
	numsum = 0
	for x in str(int(facnum)):
		numsum += int(x)
	return numsum

print countdigital(100)

# 648