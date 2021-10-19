import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []
        ans = []
        for i in range(len(nums1)):
            q.append((nums1[i]+nums2[0], i, 0))
        heapq.heapify(q)

        while len(ans) < k and q:
            t = heapq.heappop(q)
            ans.append([nums1[t[1]], nums2[t[2]]])
            if t[2] < len(nums2)-1:
                heapq.heappush(q, (nums1[t[1]]+nums2[t[2]+1], t[1], t[2]+1))

        return ans
