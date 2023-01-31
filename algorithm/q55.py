"""
典型 055 https://atcoder.jp/contests/typical90/tasks/typical90_bc
"""

# 全パターン探索だとオーダーはO(N^5)だが,係数は1/120と小さいので制限内に計算可能

import numpy as np
from numba import njit, void, i8
from sys import stdin

input = stdin.readline


@njit(void(i8, i8, i8, i8[:]), cache=True)
def main(N, P, Q, A):
    cnt = 0
    for n1 in range(N):
        for n2 in range(n1 + 1, N):
            for n3 in range(n2 + 1, N):
                for n4 in range(n3 + 1, N):
                    for n5 in range(n4 + 1, N):
                        if A[n1] * A[n2] % P * A[n3] % P * A[n4] % P * A[n5] % P == Q:
                            cnt += 1
    print(cnt)


N, P, Q = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
main(N, P, Q, A)
