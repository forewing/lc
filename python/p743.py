import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        for time in times:
            edges[time[0]-1].append((time[1]-1, time[2]))

        result = [float('inf')] * n
        result[k-1] = 0
        q = [(0, k-1)]
        heapq.heapify(q)

        while q:
            t = heapq.heappop(q)
            if result[t[1]] < t[0]:
                continue

            for edge in edges[t[1]]:
                dist = t[0] + edge[1]
                if dist < result[edge[0]]:
                    result[edge[0]] = dist
                    heapq.heappush(q, (dist, edge[0]))

        ans = max(result)
        if ans == float('inf'):
            return -1
        return ans


if __name__ == "__main__":
    s = Solution()
    s.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1)
