class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if len(s) != len(goal):
            return False
        for k in range(n):
            if s[k:] == goal[:n-k] and s[:k] == goal[n-k:]:
                return True
        return False
