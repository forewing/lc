class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for num in nums:
            target |= num
        dp = [0] * (target * 2)
        dp[0] = 1
        for num in nums:
            dp2 = dp.copy()
            for i in range(target + 1):
                dp2[i | num] += dp[i]
            dp = dp2
        return dp[target]
