# coding=utf-8

import copy

digitsnums = [str(x) for x in xrange(10)]

print digitsnums

nums = []

# for a in digitsnums:
# 	# print 'a',a
# 	num = ""
# 	num += a
# 	digitsnum = copy.copy(digitsnums) 
# 	digitsnum.remove(a)
# 	for b in digitsnum:
# 		# print 'b',b
# 		num += b
# 		digitsnu = copy.copy(digitsnum) 
# 		digitsnu.remove(b)
# 		for c in digitsnu:
# 			# print 'c',c
# 			num += c
# 			digitsn = copy.copy(digitsnu) 
# 			digitsn.remove(c)
# 			for d in digitsn:
# 				# print 'd',d
# 				num += d
# 				digits = copy.copy(digitsn) 
# 				digits.remove(d)
# 				for e in digits:
# 					num += e
# 					digit = copy.copy(digits)
# 					digit.remove(e)
# 					for f in digit:
# 						num += f
# 						digi = copy.copy(digit) 
# 						digi.remove(f)
# 						for g in digi:
# 							num += g
# 							dig = copy.copy(digi)
# 							dig.remove(g)
# 							for h in dig:
# 								num += h
# 								di = copy.copy(dig)
# 								di.remove(h)
# 								for i in di:
# 									num += i
# 									dd = copy.copy(di)
# 									dd.remove(i)
# 									for j in dd:
# 										num += j
# 										nums.append(num)



# print nums
# print len(nums)


def digitsnumsnum(num,digitsnums):
	digitsnum = copy.copy(digitsnums)
	if not digitsnums:
		return num
	else:
		for x in digitsnum:
			return digitsnumsnum(num+x,digitsnum.remove(x))



d = digitsnumsnum("",digitsnums)
print d.next()
print d.next()