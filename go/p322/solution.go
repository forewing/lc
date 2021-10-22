package p322

/*
 * @lc app=leetcode id=322 lang=golang
 */

// @lc code=start

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	dp[0] = 0

	for i := 1; i <= amount; i++ {
		dp[i] = -1
		for _, c := range coins {
			if c > i || dp[i-c] == -1 {
				continue
			}
			if dp[i] == -1 || dp[i-c]+1 < dp[i] {
				dp[i] = dp[i-c] + 1
			}
		}
	}

	return dp[amount]
}

// @lc code=end
