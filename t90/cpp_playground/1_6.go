package main

import "fmt"

// 大きい方の数値を返す
func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func solve() {
	n := 5
	a := []int{2, 3, 4, 5, 10}

	ans := 0

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				len := a[i] + a[j] + a[k]
				ma := max(a[i], max(a[j], a[k]))
				rest := len - ma

				if ma < rest {
					ans = max(ans, len)
				}
			}
		}
	}

	fmt.Printf("%d\n", ans)
}

func main() {
	solve()
}
