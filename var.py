# 14
# n = 49**6 + 7**19 - 21
# s = ''
# while n > 0:
#     s = str(n % 7) + s
#     n = n // 7
# print(s.count('0'))  # 8


# 15
# def dell(n, m):
#     return n % m == 0


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (dell(120, A) and ((not (dell(x, A))) <= (dell(x, 18) <= (not (dell(x, 24)))))) == False:
#             break
#     else:
#         print(A)  # 24


# 16
# def f(n):
#     if n == 0:
#         return 0
#     if n % 3 == 0 and n > 0:
#         return n + f(n-3)
#     if n % 3 > 0:
#         return n + f(n - (n % 3))


# print(f(26)) #134

# 17
# f = open('17 (1).txt')
# a = [int(s) for s in f]
# pari = []
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if (a[i] % 160 != a[j] % 160) and ((a[i] % 7 == 0) or (a[j] % 7 == 0)):
#             pari.append(a[i] + a[j])
# print(len(pari), max(pari))


# 23
from fnmatch import *


def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start+2, end) + task23(start+4, end)


print(task23(21, 30))  # 96


# 25
for x in range(3127, 10**9, 3127):
    if fnmatch(str(x), '12*93?1?'):
        print(x)
