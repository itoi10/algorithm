"""
典型 024 https://atcoder.jp/contests/typical90/tasks/typical90_x
"""

N, K = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

dif = sum([abs(a - b) for a, b in zip(A, B)])

# K回に間に合って余分が偶数回ならYes
if dif <= K and (K - dif) % 2 == 0:
    print("Yes")
else:
    print("No")
