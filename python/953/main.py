class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        translate = {}
        for i in range(26):
            translate[order[i]] = chr(ord('a') + i)
        words2 = []
        for word in words:
            word2 = []
            for c in word:
                word2.append(translate[c])
            words2.append("".join(word2))
        words2_sorted = sorted(words2)
        for i in range(len(words2)):
            if words2[i] != words2_sorted[i]:
                return False
        return True
