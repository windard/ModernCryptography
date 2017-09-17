# coding=utf-8

def solve(n):
    for i in xrange(2, n):
        find_prime(i)


def find_prime(n):
    for i in xrange(1, n):
        check_