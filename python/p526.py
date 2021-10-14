from collections import deque


class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        q = []
        q.append(set())
        while q:
            t = q.pop()
            tl = len(t)
            if tl == n:
                ans += 1
                continue
            for i in range(1, n + 1):
                if not i in t and (i % (tl + 1) == 0 or (tl + 1) % i == 0):
                    q.append(t | {i})
        return ans
