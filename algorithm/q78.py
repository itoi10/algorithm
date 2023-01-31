"""
典型 078 https://atcoder.jp/contests/typical90/tasks/typical90_bz
"""

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

vertex = [[] for _ in range(N)]

# 隣接リスト作成
for i in range(M):
    a, b = AB[i]
    a -= 1
    b -= 1
    vertex[a].append(b)
    vertex[b].append(a)

# 計算
rslt = 0
for i in range(N):
    cnt = 0
    for v in vertex[i]:
        if v < i:
            cnt += 1
    if cnt == 1:
        rslt += 1

print(rslt)
