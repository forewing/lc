class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while r - l > 3:
            m = (l + r) // 2
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return min(nums[l:r+1])
