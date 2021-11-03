# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        ans = []
        q = deque()
        q.append(root)
        while q:
            t = q.popleft()
            if not t:
                ans.append(None)
                continue
            ans.append(t.val)
            q.append(t.left)
            q.append(t.right)

        while ans and ans[-1] is None:
            ans.pop()

        return str(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = eval(data)
        if not arr:
            return None
        n = len(arr)

        q = deque()
        root = TreeNode(arr[0])
        q.append(root)

        i = 1
        while i < n and q:
            t = q.popleft()
            if arr[i] is not None:
                t.left = TreeNode(arr[i])
                q.append(t.left)
            i += 1
            if i < n and arr[i] is not None:
                t.right = TreeNode(arr[i])
                q.append(t.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
