# coding=utf-8

for x in xrange(1,1000):
	for y in xrange(1,1000):
		for z in xrange(1,1000):
			if x + y + z == 1000 and x**2 + y **2 == z**2:
				print x,y,z

# 200 375 425