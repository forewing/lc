class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        l = len(s)
        valid = [False] * (l + 1)
        valid[0] = True
        for i in range(l):
            if not valid[i]:
                continue
            for j in range(i + 1, l + 1):
                if not valid[j] and s[i:j] in words:
                    valid[j] = True
            if valid[l]:
                return True
        return valid[l]
