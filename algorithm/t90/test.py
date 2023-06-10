from sys import stdin
import numpy as np

input = stdin.readline

N, Q = list(map(int, input().split()))
A = np.sort(list(map(int, input().split())))


for _ in range(Q):  # 10e5
    X = int(input())
    idx = np.searchsorted(A, X)

    s1 = abs(np.sum(A[idx:]))
    s2 = abs(np.sum(A[:idx]))

    x1 = X * (N - idx)
    x2 = X * idx

    print(abs(s1 - x1) + abs(s2 - x2))


# print(index, s1, s2)

# N = int(input())

# a = [([0] * N) for _ in range(N)]

# for i in range(N):
#     for j in range(i + 1):
#         if j == 0 or j == N - 1:
#             a[i][j] = 1
#         else:
#             a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
#     print(*a[i][: i + 1])


# # ABC.sort(key=lambda v: v[2])
# from collections import defaultdict
# from sys import stdin

# input = stdin.readline
# set_ = defaultdict(int)

# for _ in range(int(input())):
#     q = input()
#     if q[0] == "1":
#         x = int(q[2:])
#         set_[x] += 1
#     elif q[0] == "2":
#         x, c = list(map(int, q[2:].split()))
#         if set_[x] > c:
#             set_[x] -= c
#         else:
#             set_.pop(x)
#     else:
#         k = set_.keys()
#         print(max(k) - min(k))


# class UnionFind:
#     def __init__(self, n):
#         self.parents = [-1] * n

#     def find_parent(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find_parent(self.parents[x])
#             return self.parents[x]

#     def union(self, x, y):
#         x = self.find_parent(x)
#         y = self.find_parent(y)
#         if x == y:
#             return
#         if self.parents[x] > self.parents[y]:
#             x, y = y, x
#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def is_same_parent(self, x, y):
#         return self.find_parent(x) == self.find_parent(y)


# uf = UnionFind(N)
# rslt = []

# for abc in ABC:
#     a, b, c, i = abc
#     a -= 1
#     b -= 1
#     if not uf.is_same_parent(a, b):
#         uf.union(a, b)
#         rslt.append(i)

# print(uf.parents)

# print(rslt)


# # N = int(input())
# # S = [input().strip() for _ in range(N)]

# # print(N, S)

# # for i in range(10*N):


# # N, K = list(map(int, input().split()))
# # A = list(map(int, input().split()))
# # B = list(map(int, input().split()))


# # dp = [10**9 + 1] * (N + 1)


# # dp[0] = 0
# # dp[1] = 0


# # for i in range(2, N + 1):

# #     if i == N:
# #         x = A[0]
# #         y = A[-1]
# #     else:
# #         x = A[i]
# #         y = A[i - 1]
# #     a = dp[i - 1] + x
# #     b = dp[i - 2] + y
# #     dp[i] = min(a, b)

# # print(dp[-1])


# # from sys import stdin

# # input = stdin.readline

# # N, W = list(map(int, input().split()))
# # A = list(map(int, input().split()))

# # print(N, W, A)

# # dp = [[0] * (N + 1) for _ in range(N + 1)]

# # for a in A:
