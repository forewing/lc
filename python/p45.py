class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        tail = 1
        for i in range(n):
            limit = min(n, i + nums[i] + 1)
            for j in range(tail, limit):
                dp[j] = min(dp[j], dp[i] + 1)
            tail = limit - 1

        return dp[-1]
