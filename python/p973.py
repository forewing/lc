import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        cnt = 0

        for i in range(len(points)):
            e = (-(points[i][0]**2 + points[i][1]**2), points[i])
            if i < k:
                q.append(e)
                continue
            elif i == k:
                heapq.heapify(q)

            heapq.heappushpop(q, e)

        return map(lambda e: e[1], q)
