class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0] * m for _ in range(n)]
        for i in range(n):
            table[i][0] = 1
        for j in range(m):
            table[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                table[i][j] += table[i-1][j] + table[i][j-1]
        return table[n-1][m-1]
