# coding=utf-8
import calendar


CreationYear = 1900
CreationMonth = 1
CreationDay = 1
CreationWeekDay = 1


def is_leap(year):
    return (not year % 4 and year % 100) or not year % 400


def calculate_sunday_first_of_month(start_day, end_day):
    count = 0
    for i in range(start_day[0], end_day[0]+1):
        for j in range(12):
            weekday = calendar.weekday(i, j+1, 1)
            if weekday == 6:
                print(i, j+1, 1)
                count += 1
    return count


def month_day(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap(year):
        return 29
    else:
        return 28


def other_calculate_sunday_first_of_month(start_day, end_day):
    start_count = False
    count = 0
    total_days = 0
    year = CreationYear
    month = CreationMonth
    while year < end_day[0]:

        while month <= 12:
            if year == start_day[0] and month == start_day[1]:
                start_count = True
                # print(year, month, 1, total_days % 7)
            if total_days % 7 == 6 and start_count:
                count += 1
                print(year, month, 1)
            total_days += month_day(year, month)
            month += 1

        month = 1
        year += 1

    while month <= end_day[1]:
        if total_days % 7 == 6 and start_count:
            count += 1
            print(year, month, 1)
        total_days += month_day(year, month)
        month += 1

    return count


if __name__ == '__main__':
    # print(calculate_sunday_first_of_month((1901,1,1), (2000,12,31)))
    print(other_calculate_sunday_first_of_month((1901,1,1), (2000,12,31)))

