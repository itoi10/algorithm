"""
典型 004 https://atcoder.jp/contests/typical90/tasks/typical90_d
"""
# 愚直に各要素の計算を行うと計算量が多すぎるので前処理を行う.
# 各要素はその行の合計値と列の合計値から重複している自身の値を
# 1回引いたものになるのであらかじめ列と行の合計値を計算しておく.

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

# 各行の合計値を計算
row_sums = [sum(row) for row in A]

# 各列の合計値を計算
col_sums = [sum([row[i] for row in A]) for i in range(W)]

# 各要素の値を計算して表示
for i in range(H):
    dist = []
    for j in range(W):
        # 行の合計値 + 列の合計値 - 要素の値
        dist.append(row_sums[i] + col_sums[j] - A[i][j])
    print(*dist)


################################################################
# 前処理の時間計測
################################################################
import timeit


def f1():
    row_sums = [sum(row) for row in A]
    col_sums = [sum([row[i] for row in A]) for i in range(W)]


def f2():
    row_sums = [0] * H
    col_sums = [0] * W
    for i in range(H):
        for j in range(W):
            row_sums[i] += A[i][j]
            col_sums[j] += A[i][j]


def f3():
    row_sums = []
    col_sums = []
    for i in range(H):
        row_sums.append(sum(A[i]))
        col_sums.append(sum([row[i] for row in A]))


num = 100000
t1 = timeit.timeit("f1()", globals=globals(), number=num)
t2 = timeit.timeit("f2()", globals=globals(), number=num)
t3 = timeit.timeit("f3()", globals=globals(), number=num)

print("f1", t1)
print("f2", t2)
print("f3", t3)
# f1 1.1285302890173625
# f2 2.451951269991696
# f3 1.2148397330020089
