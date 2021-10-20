class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        count_grid = [[0]*m for _ in range(n)]

        for i in range(n):
            start = 0
            count = 0
            for j in range(m):
                if grid[i][j] == "E":
                    count += 1
                elif grid[i][j] == "W":
                    for t in range(start, j):
                        count_grid[i][t] = count
                    start = j + 1
                    count = 0
            for t in range(start, m):
                count_grid[i][t] = count

        for j in range(m):
            start = 0
            count = 0
            for i in range(n):
                if grid[i][j] == "E":
                    count += 1
                elif grid[i][j] == "W":
                    for t in range(start, i):
                        count_grid[t][j] += count
                    start = i + 1
                    count = 0
            for t in range(start, n):
                count_grid[t][j] += count

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    ans = max(ans, count_grid[i][j])
        return ans
