"""
典型 061 https://atcoder.jp/contests/typical90/tasks/typical90_bi
"""

from collections import deque
from sys import stdin

input = stdin.readline

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

que = deque()

for t, x in TX:
    if t == 1:
        que.appendleft(x)
    elif t == 2:
        que.append(x)
    else:
        print(que[x - 1])
