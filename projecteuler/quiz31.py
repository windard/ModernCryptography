# coding=utf-8

# coins = (1, 2, 5, 10)
coins = (1, 2, 5, 10, 20, 50, 100)
# coins = (1, 2, 5, 10, 20, 50, 100, 200)
# members = iter(members)

# times = 0

# def divide_num(num, line):
#   global times
#   if num < 0:
#       return
#   if num == 0:
#       times += 1
#       print line
#       return

#   for i in members:
#       divide_num(num - i, line + ' + ' + str(i))


# def divide_num(num, line, index):
#     global times
#     if num < 0:
#         return
#     if num == 0:
#         times += 1
#         print 'success:', line
#         return
#     try:
#         # cur = members.next()
#         cur = members[index]
#     except:
#         return
#     maxnum = 201 / cur
#     for i in xrange(1, maxnum):
#         # print cur, num
#         divide_num(num - i * cur, line + ' + ' + str(i) + ' * ' + str(cur), index + 1)

def remove_duplicate(n):
    ns = []
    for i in n:
        if tuple(i) not in ns:
            ns.append(tuple(i))
    return ns
# def dec(nums):
#     print nums
#     nums.pop()

# def test(nums):
#     print nums
#     nums.pop()
#     _nums = nums[:]
#     dec(_nums)
#     # _nums = nums[:]
#     dec(nums)

# divide_num(200, '', 0)
solutions = []

def drivi_coins(nums, coins, collec):
    if nums == 0:
        solutions.append(collec)
        return
    if nums < 0:
        return
    try:
        coin = coins.pop()
    except IndexError:
        return
    while nums > 0:
        _coins = coins[:]
        _collec = collec[:]
        drivi_coins(nums, _coins, _collec)
        nums -= coin
        collec.append(coin)
        __coins = coins[:]
        __collec = collec[:]
        drivi_coins(nums, __coins, __collec)

if __name__ == '__main__':
    # test([1,2,3,4])
    coins = list(coins)
    coins.sort()
    # coins.reverse()
    drivi_coins(200, coins, [])
    # print solutions, len(solutions)
    # print remove_duplicate(solutions), len(remove_duplicate(solutions))
    print len(remove_duplicate(solutions))
    # print times

# 73682
