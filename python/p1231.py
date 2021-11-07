class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        self.sweetness = sweetness
        self.pieces = k + 1

        l = 1
        r = sum(sweetness) // (k + 1)
        while l <= r:
            m = (l + r) // 2
            if self.valid(m):
                l = m + 1
            else:
                r = m - 1

        return l - 1

    def valid(self, target):
        count = 0
        current = 0
        for x in self.sweetness:
            current += x
            if current >= target:
                count += 1
                if count >= self.pieces:
                    return True
                current = 0
        return False
