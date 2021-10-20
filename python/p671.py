# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, node):
        if not node:
            return
        if self.min1 == -1 or node.val < self.min1:
            self.min2 = self.min1
            self.min1 = node.val
        elif (self.min2 == -1 or node.val < self.min2) and node.val > self.min1:
            self.min2 = node.val
        self.search(node.left)
        self.search(node.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min1 = -1
        self.min2 = -1
        self.search(root)
        return self.min2
