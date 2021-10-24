class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1

        if n < 3:
            return [t0, t1, t2][n]

        for _ in range(2, n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2
