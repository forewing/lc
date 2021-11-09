class Solution:
    def __init__(self):
        self.low = -(1 << 31)
        self.high = (1 << 31) - 1

    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        x = int(str(x)[::-1]) * sign
        if x < self.low or x > self.high:
            return 0
        return x
