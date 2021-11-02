class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        record = set()
        for i in range(len(s) - 9):
            t = s[i:i+10]
            if t in record:
                ans.add(t)
            else:
                record.add(t)
        return list(ans)
