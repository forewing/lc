class Solution:
    def search(self, cursor, splits):
        s = ''
        for i in range(cursor, self.n):
            s += self.s[i]
            if s in self.dic:
                self.search(i+1, splits | {i})
        if s in self.dic:
            s = ''
            for i in range(self.n):
                s += self.s[i]
                if i in splits:
                    s += ' '
            self.ans.add(s)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.dic = set()
        for word in wordDict:
            self.dic.add(word)
        self.s = s
        self.n = len(s)
        self.ans = set()

        self.search(0, set())

        return list(self.ans)
