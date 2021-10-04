from collections import defaultdict


class Solution:
    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
            return self.par[a]
        return a

    def union(self, a, b):
        self.par[self.find(b)] = self.find(a)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.par = [i for i in range(n)]
        ans = ['.'] * n

        for pair in pairs:
            self.union(pair[0], pair[1])

        pars = defaultdict(list)

        for i in range(n):
            pars[self.find(i)].append(i)

        for par in pars:
            l = pars[par]
            chars = [s[i] for i in l]
            chars.sort()
            for i in range(len(l)):
                ans[l[i]] = chars[i]

        return "".join(ans)
