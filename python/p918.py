import heapq


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        min_sub = nums[0]
        max_sub = nums[0]
        tot = nums[0]

        max_heap = [-nums[0]]
        min_heap = [nums[0]]

        for i in range(1, n):
            tot += nums[i]
            min_sub = min(min_sub, tot + max_heap[0], tot)
            max_sub = max(max_sub, tot - min_heap[0], tot)
            heapq.heappush(max_heap, -tot)
            heapq.heappush(min_heap, tot)

        if tot < 0 and tot == min_sub:
            return max_sub

        return max(tot - min_sub, max_sub)
