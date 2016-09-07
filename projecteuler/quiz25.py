# coding=utf-8

def fib(n):
	a = 1
	b = 1
	c = []
	c.append(a)
	while b < n:
		c.append(b)
		a,b = b,b+a
	return c

num = "1"+"0"*999
print len(fib(int(num)))