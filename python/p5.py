class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        la = 0
        ra = 1

        l = 0
        r = n
        while l < r:
            if r - l > ra - la:
                ok = True
                lt = l
                rt = r
                while lt < rt:
                    if s[lt] == s[rt - 1]:
                        lt += 1
                        rt -= 1
                    else:
                        ok = False
                        break
                if ok:
                    la = l
                    ra = r
            r -= 1
            if l == r:
                l += 1
                r = n
        return s[la:ra]
