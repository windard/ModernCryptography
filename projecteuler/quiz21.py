# coding=utf-8

def decomposeall(n):
	res = []
	for x in xrange(1,n):
		if n%x == 0:
			res.append(x)

	return res

def findamicable(n):
	sumnum = 0
	for x in xrange(1,n):
		for y in xrange(1,n):
			if sum(decomposeall(y)) == x and sum(decomposeall(x)) == y:
				sumnum += x
				sumnum += y
	return sumnum


print findamicable(1000)
