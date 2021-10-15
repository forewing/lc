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

        l = max(self.search(node.left), self.search(node.right))
        if len(self.list) <= l:
            self.list.append([])
        self.list[l].append(node.val)
        return l + 1

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.list = []
        self.search(root)
        return self.list
