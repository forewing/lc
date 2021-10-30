class Solution:
    def longestDupSubstring(self, s: str) -> str:
        l = 1
        ans = ""
        for i in range(len(s)):
            remain = s[i+1:]
            long = s[i:i+l]
            while long in remain:
                ans = long
                l += 1
                long = s[i:i+l]
        return ans
