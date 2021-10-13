"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert_after(self, curr, node):
        node.next = curr.next
        curr.next = node

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node()
        new_node.val = insertVal

        if not head:
            new_node.next = new_node
            return new_node

        now = head
        while now.next.val >= now.val and now.next != head:
            now = now.next

        if insertVal < now.val:
            while now.next.val < insertVal:
                now = now.next

        self.insert_after(now, new_node)
        return head
