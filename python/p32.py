class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [(0, -1)]
        for i, c in enumerate(s):
            if c == '(':
                stack.append((1, i))
            else:
                if stack[-1][0] == 1:
                    stack.pop()
                    ans = max(ans, i - stack[-1][1])
                else:
                    stack[-1] = (stack[-1][0], i)
        return ans
