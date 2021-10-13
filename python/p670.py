class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        s = str(num)
        n = len(s)
        for i in range(n):
            for j in range(i):
                ts = [c for c in s]
                ts[i], ts[j] = ts[j], ts[i]
                t = int(''.join(ts))
                ans = max(ans, t)
        return ans
