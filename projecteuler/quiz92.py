# coding=utf-8

def eliminate(n):
    return sum(map(lambda x:int(x)**2, str(n)))

def solve(n):
    nums = []
    for i in xrange(1, n):
        j = i
        while 1:
            i = eliminate(i)
            if i in (1, 89):
                if i == 89:
                    nums.append(j)
                break
    return nums

if __name__ == '__main__':
    print len(solve(10000000))

# 8581146