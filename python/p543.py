# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return 0

        l = self.traverse(node.left)
        r = self.traverse(node.right)

        self.ans = max(self.ans, l + r)

        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse(root)
        return self.ans
