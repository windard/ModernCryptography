# coding=utf-8

digitalSum = lambda n: reduce(lambda x, y: x+y, map(int, list(str(n))))

# print digitalSum(123456789)

nums = []

import math

for i in xrange(100):
    for j in xrange(100):
        try:
            nums.append(digitalSum(int(math.pow(i, j))))
        except Exception, e:
            print tuple(e)
            print max(nums)

print len(nums)
print max(nums)
# 978

# print math.pow(99, 99)
# print int(math.pow(99, 99))
# print digitalSum(int(math.pow(99, 99)))
# print len('369729637649726802192985226395427290145296428445515959701359650120802601667133273280053721002700400354392780458116125965728631706472588849812738072765460822138161108630185181415759762204338929270784')
