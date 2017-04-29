# coding=utf-8


class MyList(list):

    def __eq__(self, *args, **kwargs):
        # print args, kwargs
        for i in self:
            if i not in args[0]:
                return False
            if self.count(i) != args[0].count(i):
                return False
        else:
            if len(self) == len(args[0]):
                return True
            return False

# a = 125874

# print MyList(str(a)) == MyList(str(a * 2))

for i in xrange(10000000):
    if MyList(str(i)) == MyList(str(2 * i)) == MyList(str(3 * i)) == MyList(str(4 * i)) == MyList(str(5 * i)) == MyList(str(6 * i)):
        print i

# 142857
# 1428570
# 1429857
