package p1223

const (
	mod = 1000000000 + 7
)

func dieSimulator(n int, rollMax []int) int {
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, 6)
		for j := 0; j < 6; j++ {
			dp[i][j] = make([]int, rollMax[j])
		}
	}

	for j := 0; j < 6; j++ {
		dp[0][j][0] = 1
	}

	for i := 1; i < n; i++ {
		for now := 0; now < 6; now++ {
			for pre := 0; pre < 6; pre++ {
				if now == pre {
					for t := 0; t < rollMax[now]-1; t++ {
						dp[i][now][t+1] += dp[i-1][now][t]
						dp[i][now][t+1] %= mod
					}
					continue
				}
				for t := 0; t < rollMax[pre]; t++ {
					dp[i][now][0] += dp[i-1][pre][t]
					dp[i][now][0] %= mod
				}
			}
		}
	}

	ans := 0
	for j := 0; j < 6; j++ {
		for t := 0; t < rollMax[j]; t++ {
			ans += dp[n-1][j][t]
			ans %= mod
		}
	}

	return ans
}
