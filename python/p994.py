from collections import deque


class Solution:
    def adjs(self, x, y):
        result = []
        for (xt, yt) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if xt >= 0 and yt >= 0 and xt < self.n and yt < self.m:
                result.append((xt, yt))
        return result

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])

        que = deque()
        total = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] != 0:
                    total += 1
                    if grid[i][j] == 2:
                        grid[i][j] = 1
                        que.append((i, j, 0))

        ans = 0
        while que:
            x, y, t = que.popleft()
            if grid[x][y] == 2:
                continue
            total -= 1
            grid[x][y] = 2
            ans = max(ans, t)

            for (xt, yt) in self.adjs(x, y):
                if grid[xt][yt] == 1:
                    que.append((xt, yt, t+1))

        if total != 0:
            return -1
        return ans
