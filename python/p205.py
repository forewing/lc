class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mst = {}
        mts = {}
        for i in range(len(s)):
            if s[i] in mst:
                if mst[s[i]] != t[i]:
                    return False
            else:
                mst[s[i]] = t[i]

            if t[i] in mts:
                if mts[t[i]] != s[i]:
                    return False
            else:
                mts[t[i]] = s[i]

        return True
