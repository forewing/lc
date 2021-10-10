# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        self.list.append(node.val)
        self.traverse(node.right)

    def build(self, l, r):
        if l > r:
            return None

        m = (l + r) // 2
        node = TreeNode(val=self.list[m])
        node.left = self.build(l, m-1)
        node.right = self.build(m+1, r)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.list = []
        self.traverse(root)
        return self.build(0, len(self.list) - 1)
