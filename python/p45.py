class Solution:
    def jump(self, nums: List[int]) -> int:
        self.dp = [-1] * len(nums)
        self.ok = [True] * len(nums)
        self.dp[-1] = 0
        self.nums = nums
        return self.search(0)

    def search(self, index):
        if self.dp[index] != -1 or not self.ok[index]:
            return self.dp[index]

        ok = False
        ans = float('inf')
        for next in range(index + 1, index + self.nums[index] + 1):
            if next >= len(self.nums):
                continue
            t = self.search(next)
            if t != -1:
                ans = min(ans, t)
                ok = True
        if ok:
            self.dp[index] = ans + 1
        else:
            self.ok[index] = False
        return self.dp[index]
