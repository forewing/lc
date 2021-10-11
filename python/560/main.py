from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        sum = 0
        ans = 0
        for num in nums:
            table[sum] += 1
            sum += num
            ans += table[sum - k]

        return ans
