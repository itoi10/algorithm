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
