"""
典型 014 https://atcoder.jp/contests/typical90/tasks/typical90_n
"""

from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 昇順ソート
A.sort()
B.sort()

rslt = 0
for i in range(N):
    # ソート済みの生徒iと学校iを順番に割り当てていけば交差なく最小になる
    rslt += abs(A[i] - B[i])

print(rslt)