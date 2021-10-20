class Solution:
    def isDec(self, s: str) -> bool:
        if not s:
            return False

        start = 1 if s[0] == '-' or s[0] == '+' else 0
        try:
            i = s.index('.')
            if i == start:
                return self.isDig(s[i+1:])
            elif i == len(s) - 1:
                return self.isDig(s[start:i])
            else:
                return self.isDig(s[start:i]) and self.isDig(s[i+1:])
        except ValueError as e:
            return self.isDig(s[start:])

    def isInt(self, s: str) -> bool:
        if not s:
            return False

        start = 1 if s[0] == '-' or s[0] == '+' else 0
        return self.isDig(s[start:])

    def isDig(self, s: str) -> bool:
        if not s:
            return False

        o0 = ord('0')
        o9 = ord('9')
        for o in map(ord, s):
            if o < o0 or o > o9:
                return False
        return True

    def isNumber(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                return self.isDec(s[:i]) and self.isInt(s[i+1:])
        return self.isDec(s)
