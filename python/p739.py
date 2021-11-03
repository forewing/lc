class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        s = []

        for i, t in enumerate(temperatures):
            while s and t > s[-1][1]:
                ans[s[-1][0]] = i - s[-1][0]
                s.pop()
            s.append((i, t))

        return ans
