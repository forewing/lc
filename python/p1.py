class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if num in m:
                return [m[num], i]
            m[target - num] = i
