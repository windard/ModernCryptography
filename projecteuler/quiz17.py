# # coding=utf-8

# import string

# # english = { 1:"one",
# #             2:"two",
# #             3:"three",
# #             4:"four",
# #             5:"five",
# #             6:"six",
# #             7:"seven",
# #             8:"eight",
# #             9:"nine",
# #             10:"ten",
# #             11:"eleven",
# #             12:"twelve",
# #             13:"thirteen",
# #             14:"fourteen",
# #             15:"fifteen",
# #             16:"sixteen",
# #             17:"seventeen",
# #             18:"eighteen",
# #             19:"nineteen",
# #             20:"twenty",
# #             30:"thirty",
# #             40:"forty",
# #             50:"fifty",
# #             60:'sixty',
# #             }

# # print string.letters
# # print len([i for i in 'three hundred and forty-two' if i in string.letters])

# import time
# import json
# import requests

# url = 'http://fanyi.youdao.com/openapi.do?keyfrom=f2ec-org&key=1787962561&type=data&doctype=json&version=1.1&q='

# with open('data11.txt', 'a') as f:
#     for i in xrange(1, 1001):
#         try:
#             data = requests.get(url + str(i)).json()
#             data = data['basic']['explains'][0]
#             f.write(str(i)+' '+data+' '+str(len([i for i in data if i in string.letters]))+'\n')
#             time.sleep(1)
#         except:
#             print i
#         # if i % 100 == 0:
#         #     print data

# print 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 + 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 + 6 + 9 + 9 + 11 + 10 + 10 + 9 + 11 + 11 + 10 + 6 + 9 + 9 + 11 + 10 + 10 + 9 + 11 + 11 + 10 + 5 + 8 + 8 + 10 + 9 + 9 + 8 + 10 + 10 + 9 + 5 + 8 + 8 + 10 + 9 + 9 + 8 + 10 + 10 + 9 + 5 + 8 + 8 + 10 + 9 + 9 + 8 + 10 + 10 + 9 + 7 + 10 + 10 + 12 + 11 + 11 + 10 + 12 + 12 + 11 + 6 + 9 + 9 + 11 + 10 + 10 + 9 + 11 + 11 + 10 + 6 + 9 + 9 + 11 + 10 + 10 + 9 + 11 + 11 + 10 + 10 + 16 + 16 + 18 + 17 + 17 + 16 + 18 + 18 + 17 + 16 + 19 + 19 + 21 + 21 + 20 + 20 + 22 + 21 + 21 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 10 + 16 + 16 + 18 + 17 + 17 + 16 + 18 + 18 + 17 + 16 + 19 + 19 + 21 + 21 + 20 + 20 + 22 + 21 + 21 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 12 + 18 + 18 + 20 + 19 + 19 + 18 + 20 + 20 + 19 + 18 + 21 + 21 + 23 + 23 + 22 + 22 + 24 + 23 + 23 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 22 + 25 + 25 + 27 + 26 + 26 + 25 + 27 + 27 + 26 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 11 + 17 + 17 + 19 + 18 + 18 + 17 + 19 + 19 + 18 + 17 + 20 + 20 + 22 + 22 + 21 + 21 + 23 + 22 + 22 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 11 + 17 + 17 + 19 + 18 + 18 + 17 + 19 + 19 + 18 + 17 + 20 + 20 + 22 + 22 + 21 + 21 + 23 + 22 + 22 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 10 + 16 + 16 + 18 + 17 + 17 + 16 + 18 + 18 + 17 + 16 + 19 + 19 + 21 + 21 + 20 + 20 + 22 + 21 + 21 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 18 + 21 + 21 + 23 + 22 + 22 + 21 + 23 + 23 + 22 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 12 + 18 + 18 + 20 + 19 + 19 + 18 + 20 + 20 + 19 + 18 + 21 + 21 + 23 + 23 + 22 + 22 + 24 + 23 + 23 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 22 + 25 + 25 + 27 + 26 + 26 + 25 + 27 + 27 + 26 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 12 + 18 + 18 + 20 + 19 + 19 + 18 + 20 + 20 + 19 + 18 + 21 + 21 + 23 + 23 + 22 + 22 + 24 + 23 + 23 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 22 + 25 + 25 + 27 + 26 + 26 + 25 + 27 + 27 + 26 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 11 + 17 + 17 + 19 + 18 + 18 + 17 + 19 + 19 + 18 + 17 + 20 + 20 + 22 + 22 + 21 + 21 + 23 + 22 + 22 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 19 + 22 + 22 + 24 + 23 + 23 + 22 + 24 + 24 + 23 + 21 + 24 + 24 + 26 + 25 + 25 + 24 + 26 + 26 + 25 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 20 + 23 + 23 + 25 + 24 + 24 + 23 + 25 + 25 + 24 + 11

import string
data = open('data11.txt','r').read()
print len([i for i in data if data in string.letters])

# 21124