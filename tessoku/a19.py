N, W = map(int, input().split())
w, v = zip(*[map(int, input().split()) for _ in range(N)])

dp = [[-(10 ** 15)] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(W + 1):
        if w[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

print(max(dp[N]))
