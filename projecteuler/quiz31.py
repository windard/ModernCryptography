# coding=utf-8

members = [1, 2, 5, 10, 20, 50, 100, 200]
# members = iter(members)

times = 0

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


def divide_num(num, line, index):
    global times
    if num < 0:
        return
    if num == 0:
        times += 1
        print 'success:', line
        return
    try:
        # cur = members.next()
        cur = members[index]
    except:
        return
    maxnum = 201 / cur
    for i in xrange(1, maxnum):
        # print cur, num
        divide_num(num - i * cur, line + ' + ' + str(i) + ' * ' + str(cur), index + 1)


divide_num(200, '', 0)


print times
