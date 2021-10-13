from collections import defaultdict


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.table = defaultdict(list)
        for i in range(len(wordsDict)):
            self.table[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        t1 = self.table[word1]
        t2 = self.table[word2]
        l1 = len(t1)
        l2 = len(t2)

        ans = 300000

        # t1 > t2
        l = 0
        r = 0
        while l < l1 and r < l2:
            while l < l1 and t1[l] < t2[r]:
                l += 1
            if l >= l1:
                break
            while r < l2 and t1[l] > t2[r]:
                r += 1
            ans = min(ans, t1[l] - t2[r-1])

        # t1 < t2
        l = 0
        r = 0
        while l < l1 and r < l2:
            while r < l2 and t1[l] > t2[r]:
                r += 1
            if r >= l2:
                break
            while l < l1 and t1[l] < t2[r]:
                l += 1
            ans = min(ans, t2[r] - t1[l-1])

        return ans
