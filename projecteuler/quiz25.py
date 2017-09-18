# coding=utf-8

def fib(n):
  a = 1
  b = 1
  c = []
  c.append(a)
  while b < n:
      c.append(b)
      a,b = b,b+a
  return c


num = "1"+"0"*999
print len(fib(int(num)))

# def fib():
#     a, b = 1, 1
#     yield a
#     yield b
#     while 1:
#         a, b = b, a+b
#         yield b

# def solve(n):
#     f = fib()
#     i = 1
#     while i:
#         g = f.next()
#         # print i, g
#         # if i > n:
#         #     break
#         if len(str(g)) == n:
#             print i, g
#             break
#         i += 1

# if __name__ == '__main__':
#     solve(1000)
