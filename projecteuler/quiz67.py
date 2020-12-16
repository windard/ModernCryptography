# coding=utf-8

a = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3],
]


def find_max_in_matrix(matrix):
    nums = []
    for level in matrix:
        new_nums = []
        for index, num in enumerate(level):
            left = right = num
            if 0 <= index - 1 < len(nums):
                left += nums[index-1]
            if len(nums) > index:
                right += nums[index]
            new_nums.append(max(left, right))
        print(new_nums)
        nums = new_nums

    return max(nums)


def find_max_in_matrix_in_file(filename):
    with open(filename) as f:
        nums = []
        for line in f:
            level = map(int, line.strip().split())
            new_nums = []
            for index, num in enumerate(level):
                left = right = num
                if 0 <= index - 1 < len(nums):
                    left += nums[index-1]
                if len(nums) > index:
                    right += nums[index]
                new_nums.append(max(left, right))
            print(new_nums)
            nums = new_nums

        return max(nums)


if __name__ == '__main__':
    print(find_max_in_matrix(a))
    print(find_max_in_matrix_in_file("p067_triangle.txt"))
