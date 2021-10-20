class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prods_min = nums.copy()
        prods_max = nums.copy()
        for i in range(1, n):
            prods_min[i] = min(nums[i], nums[i] * prods_min[i - 1], nums[i] * prods_max[i - 1])
            prods_max[i] = max(nums[i], nums[i] * prods_min[i - 1], nums[i] * prods_max[i - 1])

        return max(prods_max)
