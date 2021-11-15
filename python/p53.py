class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mins = 0
        sumt = 0
        ans = -float('inf')
        for num in nums:
            sumt += num
            ans = max(ans, sumt - mins)
            if sumt < mins:
                mins = sumt
        return ans
