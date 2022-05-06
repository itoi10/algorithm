"""
典型 064 https://atcoder.jp/contests/typical90/tasks/typical90_bl
"""

from sys import stdin

input = stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for _ in range(Q)]

### TLE ###
# for l, r, v in LRV:
#     # 地殻変動
#     for i in range(l - 1, r):
#         A[i] += v
#     # 不便さ計算
#     rslt = 0
#     for i in range(N - 1):
#         rslt += abs(A[i] - A[i + 1])
#     print(rslt)


# 変化があった区画の階差を求めればAのl〜rまでいちいち更新しなくて良い
diffs = [A[i+1] - A[i] for i in range(N-1)]
inconv = sum([abs(n) for n in diffs])

for l, r, v in LRV:
    l -= 1
    r -= 1
    if l != 0:
        # 左側の不便さ増減
        before = diffs[l-1]
        diffs[l-1] += v
        inconv += -abs(before) + abs(diffs[l-1])
    if r != N-1:
        # 右側の不便さ増減
        before = diffs[r]
        diffs[r] -= v
        inconv += -abs(before) + abs(diffs[r])
    print(inconv)