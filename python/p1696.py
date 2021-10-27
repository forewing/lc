import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = [(-nums[0], 0)]
        for i in range(1, n):
            while i - q[0][1] > k:
                heapq.heappop(q)
            heapq.heappush(q, (-nums[i] + q[0][0], i))
        for e in q:
            if e[1] == n - 1:
                return -e[0]
