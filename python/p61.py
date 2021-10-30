# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        n = 0
        tail = head
        last_tail = None
        target = None
        while tail:
            if k + 1 == n:
                target = head
            n += 1
            last_tail = tail
            tail = tail.next
            if target:
                target = target.next
        if not target:
            k = k % n
            target = head
            for i in range(n - k - 1):
                target = target.next

        if k == 0:
            return head

        new_head = target.next
        last_tail.next = head
        target.next = None
        return new_head
