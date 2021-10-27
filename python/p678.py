class Solution:
    class Element:
        def __init__(self, t):
            # 0: *, 1: (, 2: )
            self.t = t
            self.n = 1

    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in map(lambda c: 0 if c == "*" else 1 if c == "(" else 2, s):
            if c == 2:
                if not stack:
                    return False
                if stack[-1].t == 1:
                    stack[-1].n -= 1
                    if stack[-1].n == 0:
                        stack.pop()
                elif len(stack) >= 2:
                    stack[-2].n -= 1
                    if stack[-2].n == 0:
                        stack[-2] = stack[-1]
                        stack.pop()
                        if len(stack) >= 2:
                            stack[-2].n += stack[-1].n
                            stack.pop()
                else:
                    stack[-1].n -= 1
                    if stack[-1].n == 0:
                        stack.pop()
                continue

            if stack and stack[-1].t == c:
                stack[-1].n += 1
            else:
                stack.append(self.Element(c))

        cnt = 0
        for e in stack:
            if e.t == 0:
                cnt = max(0, cnt - e.n)
            else:
                cnt += e.n

        return cnt == 0
