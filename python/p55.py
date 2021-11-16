class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        tail = 0
        index = 0
        while index <= tail:
            tail = max(tail, index + nums[index])
            if tail >= n - 1:
                return True
            index += 1
        return False
