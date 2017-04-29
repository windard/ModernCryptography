# coding=utf-8

a = map(lambda x: x*(x+1)/2, xrange(1, 300000))
b = map(lambda x: x*(3*x-1)/2, xrange(1, 300000))
c = map(lambda x: x*(2*x-1), xrange(1, 300000))

# print a
# print b
# print c

print set(a).intersection(set(b).intersection(set(c)))

# d = set(a).intersection(set(b))

# e = set(b).intersection(set(c))

# f = set(d).intersection(set(e))

# print f

# set([1, 40755, 1533776805])
