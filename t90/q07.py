"""
典型 007 https://atcoder.jp/contests/typical90/tasks/typical90_g
"""

from sys import stdin

input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

# レートを昇順ソート
A.sort()

# 二分法
for i in B:
    left = -1
    right = N
    while right - left > 1:
        # 中間値
        mid = int((left + right) / 2)
        if i >= A[mid]:
            # 右に範囲を狭める
            left = mid
        else:
            # 左に範囲を狭める
            right = mid
    # 差が小さい方を表示
    dif1 = abs(A[left] - i) if left >= 0 else 2 << 30
    dif2 = abs(A[right] - i) if right < N else 2 << 30
    print(min(dif1, dif2))
