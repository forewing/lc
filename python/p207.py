# pre -> main

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for i in range(numCourses)]
        deg = [0 for i in range(numCourses)]

        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            deg[pre[0]] += 1

        que = deque()
        for i in range(numCourses):
            if deg[i] == 0:
                que.append(i)

        visited = 0
        while que:
            visited += 1
            head = que.popleft()
            for edge in edges[head]:
                deg[edge] -= 1
                if deg[edge] == 0:
                    que.append(edge)

        return visited == numCourses
