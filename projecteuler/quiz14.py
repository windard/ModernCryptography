# coding=utf-8

def CollatzChain(n):
	res = []
	res.append(n)
	while 1:
		if n == 1:
			break
		if n%2 == 0:
			n = n/2
			res.append(n)
		else:
			n = 3*n +1
			res.append(n)
	return res

longest = 0
for x in xrange(1,1000000):
	if len(CollatzChain(x))>longest:
		longest = len(CollatzChain(x))
		longnum = x

print longest,x,CollatzChain(longnum),len(CollatzChain(longnum))

# 525 837799
