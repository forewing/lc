from functools import reduce


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return reduce(lambda s, b: s*s*x if b == "1" else s*s, bin(n)[2:], 1) ** (1 if n > 0 else -1)
