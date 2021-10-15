# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect


class Solution:
    def search(self, node):
        if not node:
            return

        self.search(node.left)
        self.list.append(node.val)
        self.search(node.right)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.list = []
        self.search(root)
        n = len(self.list)

        if n == 1:
            return [self.list[0]]

        index = bisect.bisect_left(self.list, target)
        if index > 0 and (index >= n or target - self.list[index - 1] < self.list[index] - target):
            index -= 1

        ans = [self.list[index]]
        l = index - 1
        r = index + 1
        while len(ans) < k:
            while len(ans) < k and l >= 0 and (r >= n or target - self.list[l] <= self.list[r] - target):
                ans.append(self.list[l])
                l -= 1
            while len(ans) < k and r < n and (l < 0 or target - self.list[l] >= self.list[r] - target):
                ans.append(self.list[r])
                r += 1
        return ans
