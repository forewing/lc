class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        s2 = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n] >= n - k
