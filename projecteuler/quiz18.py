# coding=utf-8

big_tri = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23],
]

small_tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

sum_all = []

def sum_level(level, position, sum_now, triangle):
    if level >= len(triangle):
        sum_all.append(sum_now)
        return
    sum_now += triangle[level][position]
    sum_level(level+1, position, sum_now, triangle)
    sum_level(level+1, position+1, sum_now, triangle)

sum_level(0, 0, 0, big_tri)
print max(sum_all)



# sum_all = [[3],]

# [
# [3],
# [10, 7],
# [12, 14, 11, 13],
# [20, 17, 19, 23, 16, 20, 22, 16]
# ]


# def sum_level(level, position):
#     if position >= len(sum_all[-2]):
#         return
#     # sum_all[-1].append(level + sum_all[-2][position])
#     # sum_all[-1].append(level + sum_all[-2][position])
#     # for each in sum_all[-2]:
#     if position == 0:
#         sum_all[-1].append(level[position] + sum_all[-2][position])
#     elif position == len(len(sum_all[-2])) -1:
#         sum_all[-1].append(level[position] + sum_all[-2][position])
#     else:
#         sum_all[-1].append(level[position] + sum_all[-2][position])
#         sum_all[-1].append(level[position+1] + sum_all[-2][position])
#     print repr(sum_all), position
#     return sum_level(level, position+1)


# for level in small_tri[1:]:
#     sum_all.append([])
#     print '*', sum_all, level
#     sum_level(level, 0)

# print sum_all
# print max(sum_all[-1])

