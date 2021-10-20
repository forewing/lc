class Solution:
    def search(self, index, src):
        if self.visited[index] != 0:
            return False

        self.visited[index] = 1
        for e in self.es[index]:
            if src is not None and e == src:
                continue
            if not self.search(e, index):
                return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.es = [[] for _ in range(n)]

        for edge in edges:
            self.es[edge[0]].append(edge[1])
            self.es[edge[1]].append(edge[0])

        self.visited = [0] * n

        return self.search(0, None) and min(self.visited) == 1
