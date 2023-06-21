package main

import "fmt"

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	var N, W int64
	fmt.Scan(&N, &W)

	w := make([]int64, N)
	v := make([]int64, N)
	for i := int64(0); i < N; i++ {
		fmt.Scan(&w[i], &v[i])
	}

	dp := make([][]int64, N+1)
	for i := int64(0); i < N+1; i++ {
		dp[i] = make([]int64, W+1)
		for j := int64(0); j < W+1; j++ {
			dp[i][j] = -1 << 60
		}
	}

	dp[0][0] = 0
	for i := int64(1); i <= N; i++ {
		for j := int64(0); j <= W; j++ {
			if w[i-1] > j {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
			}
		}
	}

	ans := int64(0)
	for i := int64(0); i <= W; i++ {
		ans = max(ans, dp[N][i])
	}
	fmt.Println(ans)
}
