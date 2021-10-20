import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = list(map(lambda x: ord(x), letters))
        target = ord(target)

        if letters[-1] <= target:
            return chr(letters[0])

        return chr(letters[bisect.bisect(letters, target)])
