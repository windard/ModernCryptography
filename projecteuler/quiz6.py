# coding=utf-8

powerpuls = 0
for x in xrange(1,101):
	powerpuls += x**2

allsum = 0
for x in xrange(1,101):
	allsum += x

print allsum**2 - powerpuls