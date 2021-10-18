from collections import Counter
from fractions import Fraction


class Solution:
    def getKB(self, point1, point2):
        if point1[0] == point2[0]:
            return (float('inf'), point1[0])
        k = Fraction((point1[1]-point2[1]), (point1[0]-point2[0]))
        b = point1[1] - k * point1[0]
        return (k, b)

    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        if l <= 1:
            return 1

        cnt = Counter()
        for i in range(l):
            for j in range(i):
                cnt[self.getKB(points[i], points[j])] += 1

        ans = max(cnt.values())
        return (round((8 * ans + 1) ** 0.5) + 1) // 2
