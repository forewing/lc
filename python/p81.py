class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while r - l > 10:
            m = (l + r) // 2
            if nums[m] == target or nums[l] == target or nums[r] == target:
                return True
            if nums[l] == nums[m]:
                l += 1
            elif nums[l] == nums[m]:
                r -= 1
            elif nums[m] > nums[l]:
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        for num in nums[l:r+1]:
            if num == target:
                return True
        return False
