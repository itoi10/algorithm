"""
典型 010 https://atcoder.jp/contests/typical90/tasks/typical90_j
"""
# 累積和でメモ化しておく
# cf. (累積和を何も考えずに書けるようにする！)[https://qiita.com/drken/items/56a6b68edef8fc605821]

from sys import stdin
input = stdin.readline

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

# 累積和
cls_sum1 = [0] * (N+1)
cls_sum2 = [0] * (N+1)
for i in range(1,N+1):
    # 各クラスのi番目までの合計値を計算
    cls_sum1[i] = cls_sum1[i-1]
    cls_sum2[i] = cls_sum2[i-1]
    if CP[i-1][0] == 1:
        cls_sum1[i] += CP[i-1][1]
    else:
        cls_sum2[i] += CP[i-1][1]

# 結果表示
for l, r in LR:
    s1 = cls_sum1[r] - cls_sum1[l-1]
    s2 = cls_sum2[r] - cls_sum2[l-1]
    print(s1, s2)