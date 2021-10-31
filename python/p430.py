"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def _flatten(self, head):
        ptr = head
        ptr_prev = None
        while ptr:
            child_head, child_tail = self._flatten(ptr.child)
            if not child_head:
                ptr_prev = ptr
                ptr = ptr.next
                continue

            if ptr.next:
                ptr.next.prev = child_tail
                child_tail.next = ptr.next

            ptr.next = child_head
            child_head.prev = ptr
            ptr.child = None

            ptr_prev = child_tail
            ptr = child_tail.next

        return head, ptr_prev

    def traverse(self, node):
        if not node:
            return
        self.list.append(node.val)
        self.traverse(node.child)
        self.traverse(node.next)

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        self.list = []
        self.traverse(head)
        ptr = head
        head.child = None
        for num in self.list[1:]:
            ptr.next = Node(num, ptr, None, None)
            ptr = ptr.next
        return head
