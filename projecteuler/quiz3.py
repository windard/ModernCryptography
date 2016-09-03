# coding=utf-8

import math

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

# print decompose(6857)
print decompose(600851475143)

def genePrime():
	primes = []
	n = 2
	primes.append(n)
	yield n
	n += 1
	primes.append(n)
	yield n
	while 1:
		while 1:
			n += 2
			for i in primes:
				if n % i == 0:
					break
			else:
				primes.append(n)
				yield n

# def decompose(n):
# 	g = genePrime()
# 	p = g.next()
# 	res = []
# 	while p < n:
# 		while n % p == 0:
# 			n = n / p
# 			res.append(p)
# 		p = g.next()
# 	if n != 1 : res.append(int(n))
# 	return res

# print decompose(600851475143)

