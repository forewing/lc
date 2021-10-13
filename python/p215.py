import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = [nums[i] for i in range(k)]
        heapq.heapify(q)
        for i in range(k, len(nums)):
            heapq.heappushpop(q, nums[i])
        return heapq.heappop(q)
