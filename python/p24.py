# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        root = ListNode(0, head)
        ptr = root
        while ptr.next and ptr.next.next:
            t = ptr.next
            ptr.next = t.next
            t.next = ptr.next.next
            ptr.next.next = t
            ptr = t

        return root.next
