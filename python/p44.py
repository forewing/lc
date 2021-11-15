class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.dp = [[-1] * len(self.p) for _ in range(len(self.s))]
        return self.tryMatch(0, 0) == 1

    def tryMatch(self, si, pi):
        if si == len(self.s) and pi == len(self.p):
            return 1
        if si == len(self.s):
            for i in range(pi, len(self.p)):
                if self.p[i] != '*':
                    return 0
            return 1
        if pi == len(self.p):
            return 0

        if self.dp[si][pi] != -1:
            return self.dp[si][pi]

        if self.s[si] == self.p[pi] or self.p[pi] == '?':
            self.dp[si][pi] = self.tryMatch(si + 1, pi + 1)
        elif self.p[pi] == '*':
            self.dp[si][pi] = 0
            if self.tryMatch(si + 1, pi) == 1 or self.tryMatch(si, pi + 1) == 1:
                self.dp[si][pi] = 1
        else:
            self.dp[si][pi] = 0

        return self.dp[si][pi]
