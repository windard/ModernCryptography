# coding=utf-8

import math

def countnum(num):
	numsum = 0
	result = []
	for x in xrange(1,num+1):
		numsum += x
		result.append(numsum)
	return result

def decompose(n):
	i = 1
	res = []
	while i < math.sqrt(n):
		i += 1
		if n % i == 0:
			n = n / i
			res.append(i)
			i = 1
	res.append(int(n))
	return res

# print decompose(countnum(7)[-1])

def decomposeall(n):
	res = []
	for x in xrange(1,n+1):
		if n%x == 0:
			res.append(x)

	return res

# print decomposeall(countnum(7)[-1])

n = 1
numsum = 0
while 1:
	numsum += n
	# print n,numsum,decomposeall(numsum),len(decomposeall(numsum))
	if len(decomposeall(numsum)) > 500 :
		print n,numsum,decomposeall(numsum)
		print 
		break
	n += 1
	if n%100==0:
		print n,numsum,len(decomposeall(numsum))
