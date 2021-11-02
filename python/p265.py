class Solution:
    def minCostII(self, costs):
        n = len(costs)
        m = len(costs[0])
        dp = [[0] * m for _ in range(n)]
        record = [costs[0][i] for i in range(m)]
        for i in range(1, n):
            l1, l2 = 0, 1
            if record[0] > record[1]:
                l1, l2 = 1, 0
            for j in range(2, m):
                if record[j] <= record[l1]:
                    l1, l2 = j, l1
                elif record[j] < record[l2]:
                    l2 = j
            v1, v2 = record[l1], record[l2]
            for j in range(0, m):
                if j == l1:
                    record[j] = costs[i][j] + v2
                else:
                    record[j] = costs[i][j] + v1

        return min(record)


if __name__ == "__main__":
    s = Solution()
    s.minCostII(
        [[3, 14, 12, 2, 20, 16, 12, 2],
         [9, 6, 9, 8, 2, 9, 20, 18],
         [20, 2, 20, 4, 5, 12, 11, 11],
         [16, 3, 7, 5, 15, 2, 2, 4],
         [17, 3, 11, 1, 9, 5, 7, 11]])
