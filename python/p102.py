from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([(root, 0)])
        while q:
            t = q.popleft()
            if len(result) <= t[1]:
                result.append([])
            result[t[1]].append(t[0].val)
            if t[0].left:
                q.append((t[0].left, t[1] + 1))
            if t[0].right:
                q.append((t[0].right, t[1] + 1))
        return result
