from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        deg = [0] * n
        edges = [[] for i in range(n)]

        for pre in prerequisites:
            deg[pre[0]] += 1
            edges[pre[1]].append(pre[0])

        que = deque()
        for i in range(n):
            if deg[i] == 0:
                que.append(i)

        ans = []

        cnt = 0
        while que:
            cnt += 1
            top = que.popleft()
            ans.append(top)
            for edge in edges[top]:
                deg[edge] -= 1
                if deg[edge] == 0:
                    que.append(edge)

        if cnt != n:
            return []

        return ans
