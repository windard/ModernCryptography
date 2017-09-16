# coding=utf-8

def check_decimal(n):
    for i in xrange(len(n)/2):
        if n[i] != n[len(n)-i-1]:
            return False
    else:
        return True

# print check_decimal('10001')
# print check_decimal('1001')
# print check_decimal('101')
# print check_decimal('11')
# print check_decimal('1')

# print check_decimal('10982')
# print check_decimal('1092')
# print check_decimal('102')
# print check_decimal('12')


def dec2bin(n):
    return bin(n)[2:]

def solve(n):
    nums = []
    for i in xrange(1, n):
        if not check_decimal(str(i)):
            continue
        if not check_decimal(dec2bin(i)):
            continue
        nums.append(i)
    return nums

if __name__ == '__main__':
    # print check_decimal('585')
    # print dec2bin(585)
    # print check_decimal(dec2bin(585))
    print sum(solve(1000000))