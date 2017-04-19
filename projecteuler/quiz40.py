# coding=utf-8

data = ''

for i in xrange(1000000):
    data += str(i)

print data[1]
print data[10]
print data[100]
print data[1000]
print data[10000]
print data[100000]
print data[1000000]

print int(data[1]) * int(data[10]) * int(data[100]) * int(data[1000]) * int(data[10000]) * int(data[100000]) * int(data[1000000])
