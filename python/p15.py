from collections import defaultdict


class Solution:
    def threeSum(self, nums):
        nums.sort()

        n = len(nums)
        pos = {}
        result = set()

        for i in range(n):
            pos[nums[i]] = i

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue

                target = -nums[i] - nums[j]
                if target in pos and pos[target] > j:
                    result.add((nums[i], nums[j], target))

        return list(result)
