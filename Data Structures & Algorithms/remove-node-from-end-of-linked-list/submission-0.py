# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        prev = slow
        fast = head
        # move fast to N
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next
        
        # move until fast is None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # remove
        if prev == slow:
            head = head.next
            slow.next = None
        else:
            temp = slow.next
            prev.next = temp
            slow.next = None

        return head        