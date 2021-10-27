class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        pos, neg = 0, 0
        if nums[0] > 0:
            pos = 1
            ans = 1
        elif nums[0] < 0:
            neg = 1

        for i in range(1, n):
            if nums[i] > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            elif nums[i] < 0:
                if neg > 0:
                    neg, pos = pos + 1, neg + 1
                else:
                    neg = pos + 1
                    pos = 0
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)

        return ans
