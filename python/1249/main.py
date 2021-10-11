class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sl = list(s)
        l = len(sl)
        cnt = 0
        for i in range(l):
            if sl[i] == '(':
                cnt += 1
            elif sl[i] == ')':
                if cnt == 0:
                    sl[i] = ''
                else:
                    cnt -= 1
        cnt = 0
        for i in range(l - 1, -1, -1):
            if sl[i] == ')':
                cnt += 1
            elif sl[i] == '(':
                if cnt == 0:
                    sl[i] = ''
                else:
                    cnt -= 1

        return "".join(sl)
