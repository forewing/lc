class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = r = root
        lc = rc = 1
        while l.left:
            l = l.left
            lc += 1
        while r.right:
            r = r.right
            rc += 1

        if lc == rc:
            return 2 ** lc - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
