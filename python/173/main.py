# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        self.list.append(node.val)
        self.traverse(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        self.traverse(root)
        self.n = len(self.list)
        self.i = 0

    def next(self) -> int:
        ret = self.list[self.i]
        self.i += 1
        return ret

    def hasNext(self) -> bool:
        return self.i < self.n
