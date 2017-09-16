# coding=utf-8


# def check_fit(nums):
#     nums = [int(i) for i in ''.join(map(str, nums))]
#     nums.sort()
#     return all(map(lambda x: x[0]==x[1], zip(nums, xrange(1, 10))))

def check_fit(nums):
    nums = set(''.join(map(str, nums)))
    fits = set(''.join(map(str, xrange(1, 10))))
    return len(nums) == 9 and nums == fits


def solve(a, b):
    fit_nums = []
    for i in xrange(a, b):
        nums = []
        for j in xrange(1, 10):
            nums.append(i*j)
            if len(''.join(map(str, nums))) > 9:
                nums.pop()
                break
        if check_fit(nums):
            # print i, nums, ''.join(map(str, nums))
            fit_nums.append(int(''.join(map(str, nums))))
    return max(fit_nums)

if __name__ == '__main__':
    print solve(1, 9999)