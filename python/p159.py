class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = [[s[0], 1]]
        for c in s[1:]:
            if c == l[-1][0]:
                l[-1][1] += 1
            else:
                l.append([c, 1])

        ans = l[0][1]
        curr = ans
        active = set([l[0][0]])
        for i in range(1, len(l)):
            if l[i][0] in active:
                curr += l[i][1]
            else:
                active = set([l[i-1][0], l[i][0]])
                curr = l[i-1][1] + l[i][1]
            ans = max(ans, curr)

        return ans
