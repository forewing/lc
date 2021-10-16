from collections import defaultdict


class Solution:
    def search(self, target, start):
        if target < 0:
            return False
        if target in self.ava:
            return self.ava[target]

        self.ava[target] = False
        for i in range(start, self.n):
            if self.search(target - self.nums[i], i + 1):
                self.ava[target] = True
                return True

    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0:
            return False

        self.nums = nums
        self.n = len(nums)
        self.ava = defaultdict(bool)
        self.ava[0] = True
        return self.search(tot // 2, 0)
