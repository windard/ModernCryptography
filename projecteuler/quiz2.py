# coding=utf-8

def fib(n):
	a = 1
	b = 2
	c = []
	c.append(a)
	while b < n:
		c.append(b)
		a,b = b,b+a
	return c

print sum(filter(lambda i:i%2==0,fib(4000000)))