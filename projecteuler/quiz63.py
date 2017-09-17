# coding=utf-8

def check_max_pow(num):
    pows = []
    for i in xrange(100):
        if len(str(num ** i)) == i:
            pows.append(i)
    return pows

def check_max_num(num, pows):
    result = []
    for i in pows:
        if len(str(num ** i)) == i:
            result.append(i)
    return result

def solve():
    i = 1
    digitals = []
    while 1:
        pows = check_max_pow(i)
        max_num = check_max_num(i, pows)
        digitals.extend(max_num)
        i += 1
        print i, max_num
        if len(max_num) <= 0:
            break
    return digitals

if __name__ == '__main__':
    print len(solve())
