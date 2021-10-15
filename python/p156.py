# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, node):
        if not node:
            return None

        if not node.left and not node.right:
            return node

        ret = self.search(node.left)

        if node.left:
            node.left.right = node
            node.left.left = node.right

        node.left = None
        node.right = None

        return ret

    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.search(root)
