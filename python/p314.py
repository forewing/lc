# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def traverse(self, node, col, row):
        if not node:
            return

        if len(self.col2list[col]) == 0:
            self.cols.append(col)
        self.col2list[col].append((row, node.val))

        self.traverse(node.left, col - 1, row + 1)
        self.traverse(node.right, col + 1, row + 1)

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.col2list = collections.defaultdict(list)
        self.cols = []

        self.traverse(root, 0, 0)
        self.cols.sort()

        ans = []
        for col in self.cols:
            anst = []
            self.col2list[col].sort(key=lambda e: e[0])
            for e in self.col2list[col]:
                anst.append(e[1])
            ans.append(anst)
        return ans
