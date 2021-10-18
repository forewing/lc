class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        transform = [[1, 2], [0, 2], [0, 1]]
        n = len(costs)

        dp = [[0] * 3 for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i-1][transform[j][0]], dp[i-1][transform[j][1]])
        return min(dp[n-1])
