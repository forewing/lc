class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        ans = 0
        tail = -1
        for i, c in enumerate(s):
            if c in record and record[c] > tail:
                tail = record[c]
            record[c] = i
            ans = max(ans, i - tail)
        return ans
