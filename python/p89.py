from functools import reduce


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return reduce(lambda l, n: l + list(map(lambda x: x + (1 << n), l))[::-1], range(n), [0])
