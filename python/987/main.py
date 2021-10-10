# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def traverse(self, node, row, col):
        if not node:
            return

        self.lists[col].append((row, node.val))

        self.traverse(node.left, row + 1, col - 1)
        self.traverse(node.right, row + 1, col + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.lists = defaultdict(list)
        self.traverse(root, 0, 0)

        l = 0
        r = 0

        for col in self.lists:
            l = min(l, col)
            r = max(r, col)
            self.lists[col].sort()

        ans = []
        for i in range(l, r + 1):
            ans.append([])
            for t in self.lists[i]:
                ans[-1].append(t[1])

        return ans
