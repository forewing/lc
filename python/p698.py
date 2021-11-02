class Solution:
    def canPartitionKSubsets(self, nums, k):
        if k == 1:
            return True

        s = sum(nums)
        if s % k != 0:
            return False

        self.target = s // k
        nums.sort()
        self.nums = nums
        return self.search(len(nums) - 2, k, self.target - nums[-1])

    def search(self, index, k_left, sum_left):
        if sum_left == 0:
            if k_left == 2:
                return True
            while index >= 0 and self.nums[index] == -1:
                index -= 1
            return self.search(index, k_left - 1, self.target)

        for i in range(index, -1, -1):
            if self.nums[i] == -1:
                continue
            if sum_left >= self.nums[i]:
                t = self.nums[i]
                self.nums[i] = -1
                if self.search(index, k_left, sum_left - t):
                    return True
                self.nums[i] = t

        return False
