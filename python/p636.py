class Solution:
    def parse(self, s):
        i, start, ts = s.split(":")
        return int(i), start == "start", int(ts)

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        # [id, time]
        lastts = 0
        laststart = False
        for log in logs:
            i, start, ts = self.parse(log)
            if start:
                if stack:
                    stack[-1][1] += ts - lastts
                    if not laststart:
                        stack[-1][1] -= 1
                stack.append([i, 0])
            else:
                lastcall = stack.pop()
                ans[lastcall[0]] += lastcall[1] + (ts - lastts)
                if laststart:
                    ans[lastcall[0]] += 1
            lastts = ts
            laststart = start

        return ans
