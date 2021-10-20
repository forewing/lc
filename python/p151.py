class Solution:
    def reverseWords(self, s: str) -> str:
        " ".join(map(lambda w: w[::-1], s.split()))
