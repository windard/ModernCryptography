# coding=utf-8

def much_mul(n):
    num = 1
    for i in xrange(n):
        num *= 2
        num = int(str(num)[-10:])
    return num

def main():
    num = much_mul(7830457)
    return num * 28433 + 1

if __name__ == '__main__':
    num = main()
    print num, str(num)[-10:]
    # print much_mul(5)

# 275808739992577 8739992577