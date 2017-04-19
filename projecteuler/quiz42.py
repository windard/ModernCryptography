# coding=utf-8

triangle_numbers = []

for i in xrange(50):
    triangle_numbers.append(1/2.0 * i * (i + 1))

# print triangle_numbers


with open('p042_words.txt', 'r') as f:
    data = f.read()

words = data.replace('"', '').split(',')

# print len(words)

import string

word_sum = 0
for word in words:
    wordNum = 0
    for i in word:
        wordNum += string.uppercase.index(i) + 1
    if wordNum in triangle_numbers:
        word_sum += 1

print word_sum
