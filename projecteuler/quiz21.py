# coding=utf-8

def decomposeall(n):
    res = []
    for x in xrange(1,n):
        if n%x == 0:
            res.append(x)

    return res

# def findamicable(n):
#   for x in xrange(1,n):
#       for y in xrange(1,n):
#           if sum(decomposeall(y)) == x and sum(decomposeall(x)) == y:
#               sum_all.append([x, y])


def find_damicable(n):
    for m in xrange(n):
        s = sum(decomposeall(m))
        if sum(decomposeall(s)) == m and s != m:
            sum_all.append(s)
            sum_all.append(m)

sum_all = []
# print sum(decomposeall(220))
# print sum(decomposeall(284))

find_damicable(10001)
print sum(set(sum_all))
