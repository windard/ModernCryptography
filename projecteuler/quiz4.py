# coding=utf-8

def palindromic(n):
	for x in xrange(len(str(n))/2):
		if str(n)[x] != str(n)[len(str(n)) - x - 1]:
			return False
	return True

b = 1
for i in xrange(100,999):
	for j in xrange(100,999):
		a = i*j
		if palindromic(a) and  b < a :b = a 

print i,j
print b
