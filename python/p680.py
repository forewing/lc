class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        l = len(s)
        badi = 0
        for i in range(l):
            if s[i] != s[-1-i]:
                badi = i
                break

        for i in [badi, l - badi - 1]:
            t = s[:i] + s[i+1:]
            if t == t[::-1]:
                return True

        return False
