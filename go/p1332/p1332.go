package p1332

/*
 * @lc app=leetcode id=1332 lang=golang
 */

// @lc code=start

func removePalindromeSub(s string) int {
	l := len(s)
	if l == 0 {
		return 0
	}

	for i := 0; i < l/2; i++ {
		if s[i] != s[l-1-i] {
			return 2
		}
	}

	return 1
}

// @lc code=end
