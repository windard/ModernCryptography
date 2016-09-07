# coding=utf-8

def division(n):
	return n == sum([int(x)**len(str(n)) for x in str(n)])

print sum([x for x in xrange(10000,100001) if division(x)])