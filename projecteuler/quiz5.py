# coding=utf-8

def decompose(n):
	i = 1
	res = []
	while i < n:
		i += 1
		if n % i == 0:
			n = n / i
			res.append(i)
			i = 1
	return res

# 因式分解法 
def minifator(a,b):
	c = decompose(a)
	d = decompose(b)
	e = [1]
	res = 1
	for x in c:
		if x in d and x not in e:
			e.append(x)
	for x in e:
		res *= x
	return res

# 因式分解法
def minimulti(a,b):
	c = decompose(a)
	d = decompose(b)
	res = 1
	for x in c:
		res *= x
		if x in d:
			d.remove(x)
	for x in d:
		res *= x
	return res


# 欧几里得法 递归写法
def recursive_Euclidean(a,b):
	return a if b == 0 else Euclidean( b , a % b )

# 欧几里得法 非递归写法
def Euclidean(a,b):
	while b != 0:
		a , b = b , a % b
	return a
	
# 公式法
def minimultiple(a,b):
	return a * b / Euclidean(a,b)
	
# 非递归写法
def recursive_minimultiples(n):
	res = 1
	for x in n:
		res = minimulti(res,x)
	return res

# 递归写法
def minimultiples(n):
	return n.pop() if len(n) == 1 else minimulti(n.pop(),minimultiples(n))

print minimultiples([x for x in xrange(1,20)])

# 232792560