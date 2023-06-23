S = input()
N = len(S)
T = input()
M = len(T)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N+1):
    for j in range(M+1):
        if i >= 1 and j >= 1 and S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        elif i >=1 and j >= 1:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i >= 1:
            dp[i][j] = dp[i-1][j]
        elif j >= 1:
            dp[i][j] = dp[i][j-1]

print(dp[N][M])
