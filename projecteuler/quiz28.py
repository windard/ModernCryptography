# coding=utf-8

# 2 - 4 - 6

# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

def calc(num):
    width = 1
    amount = 1
    least = 1

    while width <= (num - 1) / 2:
        gap = width * 2
        amount += (1 + 2 + 3 + 4) * gap + 4 * least 
        least = least + gap * 4
        width += 1

    return amount

print calc(1001)