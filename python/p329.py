class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.ans = [[-1] * self.m for _ in range(self.n)]
        self.matrix = matrix

        ans = 1
        for i in range(self.n):
            for j in range(self.m):
                ans = max(ans, self.search(i, j))
        return ans

    def search(self, x, y):
        if self.ans[x][y] != -1:
            return self.ans[x][y]

        self.ans[x][y] = 1
        for x2, y2 in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if x2 < 0 or y2 < 0 or x2 >= self.n or y2 >= self.m:
                continue
            if self.matrix[x2][y2] > self.matrix[x][y]:
                self.ans[x][y] = max(self.ans[x][y], self.search(x2, y2) + 1)

        return self.ans[x][y]
