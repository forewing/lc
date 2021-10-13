class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)
        for i in range(l - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                continue
            nums[i:] = nums[:i-l-1:-1]
            for j in range(i, l):
                if nums[j] > nums[i - 1]:
                    nums[j], nums[i - 1] = nums[i - 1], nums[j]
                    break
            return
        nums[:] = nums[::-1]
        return
