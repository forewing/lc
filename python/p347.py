import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter()
        for num in nums:
            cnt[num] += 1

        q = []
        keys = list(cnt.keys())
        for i in range(k):
            q.append((cnt[keys[i]], keys[i]))
        heapq.heapify(q)

        for i in range(k, len(keys)):
            heapq.heappushpop(q, (cnt[keys[i]], keys[i]))

        return map(lambda x: x[1], q)
