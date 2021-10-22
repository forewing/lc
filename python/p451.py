from collections import Counter
from functools import reduce


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(
            reduce(
                lambda l, i: l + [i[1]] * -i[0],
                sorted([(-v, k) for k, v in Counter(s).items()]),
                []
            )
        )
