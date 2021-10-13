import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.l = len(w)
        self.p = []
        self.tot = 0
        for x in w:
            self.tot += x
            self.p.append(self.tot)

    def pickIndex(self) -> int:
        r = random.randrange(0, self.tot)
        return bisect.bisect(self.p, r)
