#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, node):
        if not node:
            return 0

        l = self.search(node.left)
        r = self.search(node.right)

        self.ans = max(self.ans, node.val + max(0, l) + max(0, r))
        return node.val + max(0, l, r)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -300000000
        self.search(root)
        return self.ans
# @lc code=end
