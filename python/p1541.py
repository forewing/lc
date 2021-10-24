class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in s.replace("))", "]"):
            if c == "(":
                cnt += 1
                continue

            if c == ")":
                ans += 1

            if cnt == 0:
                ans += 1
            else:
                cnt -= 1

        return ans + cnt * 2
