# coding=utf-8

varsum = 0
for i in xrange(1,1000):
	if i%3==0 or i%5==0:
		varsum +=i

print varsum