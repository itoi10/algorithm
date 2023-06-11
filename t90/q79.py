"""
典型 079 https://atcoder.jp/contests/typical90/tasks/typical90_ca
"""

from sys import stdin

input = stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

operation_cnt = 0

# (0,0)から(H-1,W-1)まで揃えていく
for i in range(H - 1):
    for j in range(W - 1):
        diff = B[i][j] - A[i][j]
        # 差があれば操作
        if diff != 0:
            A[i][j] += diff
            A[i + 1][j] += diff
            A[i][j + 1] += diff
            A[i + 1][j + 1] += diff
            operation_cnt += abs(diff)

# 操作後,下段と右列も揃っているか?
# ok = True
# for i in range(H):
#     if A[i][W - 1] != B[i][W - 1]:
#         ok = False
# for i in range(W):
#     if A[H - 1][i] != B[H - 1][i]:
#         ok = False

# リストは==で比較可能
ok = A == B

if ok:
    print("Yes")
    print(operation_cnt)
else:
    print("No")
