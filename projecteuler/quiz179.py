# coding=utf-8

import math
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def find_all_factor(n):
	result = set()
	for i in range(1, int(math.sqrt(n))+1):
		factor = 1.0 * n / i
		if factor == int(factor):
			result.add(i)
			result.add(int(factor))
	return result


def calculate_result(start, end):
	result = []
	for i in range(start, end):
		lenn = len(find_all_factor(i))
		if lenn and lenn == len(find_all_factor(i + 1)):
			# print(i, lenn)
			result.append(i)
	return result


def concurrent_calculate(n, length=10):
	total_futures = []
	total_results = []
	step = n/length
	with ProcessPoolExecutor(length) as pool:
		for i in range(2, n, step):
			total_futures.append(pool.submit(calculate_result, i, min(i+step, n)))

	for future in futures.as_completed(total_futures):
		total_results.extend(future.result())

	print(len(total_results))


def other_concurrent_calculate(n, length=10):
	total_start = []
	total_end = []
	step = n/length
	for i in range(2, n, step):
		total_start.append(i)
		total_end.append(min(i + step, n))

	with ProcessPoolExecutor(length) as pool:
		total_results = list(pool.map(calculate_result, total_start, total_end))

	result = reduce(lambda x, y: x+y, total_results)
	# print(result)
	print(len(result))


if __name__ == '__main__':

	# print(len(calculate_result(2, 100)))
	# print(len(calculate_result(2, 10000)))
	# concurrent_calculate(100)
	# concurrent_calculate(10000)
	# concurrent_calculate(10000000)
	other_concurrent_calculate(100)
	other_concurrent_calculate(10000)
