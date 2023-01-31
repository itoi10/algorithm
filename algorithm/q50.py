"""
典型 050 https://atcoder.jp/contests/typical90/tasks/typical90_ax
"""

N, L = map(int, input().split())

# 動的計画法
dp = [0] * (N + 1)

for i in range(N + 1):
    # L段目までは1段づつしか登れない
    if i < L:
        dp[i] = 1
        continue

    # 1段前から登るパターン + L段前から登るパターン
    dp[i] = dp[i - 1] + dp[i - L]

print(dp[-1] % ((10 ** 9) + 7))
