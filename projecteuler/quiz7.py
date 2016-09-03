# coding=utf-8

# 10 001

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

g = genePrime()
for x in xrange(1,10001):
	g.next()

print g.next()