from functools import reduce


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        lookup = {k: i for i, k in enumerate(keyboard)}
        return reduce(
            lambda result, new: (result[0] + abs(result[1] - new), new),
            map(lambda c: lookup[c], word),
            (0, 0)
        )[0]
