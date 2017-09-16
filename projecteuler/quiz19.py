# coding=utf-8

def is_leap(year):
    return (not year%4 and year%100) or not year%400


def check_year(first_day, year):
    if first_day == 7:
