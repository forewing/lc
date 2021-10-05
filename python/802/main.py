from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        redges = [[] for _ in range(n)]
        outdeg = [0] * n
        for src in range(n):
            for dest in graph[src]:
                outdeg[src] += 1
                redges[dest].append(src)

        que = deque()
        for i in range(n):
            if outdeg[i] == 0:
                que.append(i)

        ans = []
        while que:
            top = que.popleft()
            ans.append(top)
            for edge in redges[top]:
                outdeg[edge] -= 1
                if outdeg[edge] == 0:
                    que.append(edge)

        ans.sort()
        return ans
