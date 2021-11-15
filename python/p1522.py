"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def _diameter(self, root) -> int:
        if not root:
            return 0

        max1 = -1
        max2 = -1
        for c in root.children:
            t = self._diameter(c)
            if t > max1:
                max1, max2 = t, max1
            elif t > max2:
                max2 = t

        if max1 == -1:
            return 1

        if max2 == -1:
            self.ans = max(self.ans, max1)
        else:
            self.ans = max(self.ans, max1 + max2)

        return max1 + 1

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        self._diameter(root)
        return self.ans
