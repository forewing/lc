class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = []
        p2 = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1.append(i)
            if wordsDict[i] == word2:
                p2.append(i)

        ans = float('inf')

        n1 = len(p1)
        n2 = len(p2)
        i1 = i2 = 0
        while i1 < n1 and i2 < n2:
            while i1 < n1 and p1[i1] < p2[i2]:
                i1 += 1
            if i1 >= n1:
                break
            ans = min(ans, p1[i1] - p2[i2])
            i2 += 1

        i1 = i2 = 0
        while i1 < n1 and i2 < n2:
            while i2 < n2 and p2[i2] < p1[i1]:
                i2 += 1
            if i2 >= n2:
                break
            ans = min(ans, p2[i2] - p1[i1])
            i1 += 1

        return ans
