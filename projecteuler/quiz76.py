# coding=utf-8
# dfs

def split_num(num):
	if num < 2:
		return 0
	elif num == 2:
		return 1
	else:
		return split_num()


def dfs(n):
	# Backtracking

	def trace():
		return
	return


def count_cum(n):
	count = [0]*(n+1)
	count[0] = 1

	for i in range(1, n):
		for j in range(i, n+1):
			count[j] += count[j-i]

			print('- dp[',j,']+= dp[',j-i, '] ,', count)
		print('*', count)
	return count[n]

"""
-  				0	  	 1 			2 			3 		4 			5
0               1        0          0           0       0           0
1 				         1(1)       1(1)       1(1)       1(1)       1(1)  : dp[n] += dp[n-1]
1,2 			                    1(2)       1(2)       2(3)       2(3)  : dp[n] += dp[n-2]   ---------n=3 截止
1,2,3                                          1(3)       1(4)       2(5)  : dp[n] += dp[n-3]   ---------n=4 截止
1,2,3,4                                                   1(5)       1(6)  : dp[n] += dp[n-4]   ---------n=5 截止

最终结果中，dp 的值会比实际可行解大一个，需要及时终止就可以取到实际值
需要每次轮训递归递加，才能避免重复，否则重复无法避免
"""


if __name__ == '__main__':
	# print(split_num(5))
	# print(split_num(100))
	print(count_cum(3))
	print(count_cum(4))
	print(count_cum(5))
	# print(count_cum(100))
