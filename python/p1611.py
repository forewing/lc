class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        for i in range(31, -1, -1):
            if n & (1 << i):
                return 2 ** (i + 1) - 1 - self.minimumOneBitOperations(n ^ (1 << i))
        return 0
