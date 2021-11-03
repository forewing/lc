from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        l = [[s[0], 1]]
        for c in s[1:]:
            if c == l[-1][0]:
                l[-1][1] += 1
            else:
                l.append([c, 1])

        ans = l[0][1]
        cnt = ans
        active = defaultdict(int)
        active[l[0][0]] = 1
        tail = 0
        for i in range(1, len(l)):
            active[l[i][0]] += 1
            cnt += l[i][1]

            while len(active) > k:
                active[l[tail][0]] -= 1
                if active[l[tail][0]] == 0:
                    del active[l[tail][0]]
                cnt -= l[tail][1]
                tail += 1

            ans = max(ans, cnt)

        return ans
