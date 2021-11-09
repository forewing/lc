class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        self.map = [0] * n
        self.edges = [[] for _ in range(n)]

        for path in paths:
            self.edges[path[0]-1].append(path[1]-1)
            self.edges[path[1]-1].append(path[0]-1)

        self.n = n
        self.search(0)

        return self.map

    def search(self, current):
        if current == self.n:
            return True

        ava = [True] * 5
        for e in self.edges[current]:
            ava[self.map[e]] = False

        for i in range(1, 5):
            if not ava[i]:
                continue
            self.map[current] = i
            if self.search(current + 1):
                return True

        return False
