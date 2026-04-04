# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            if fast.next == slow or fast.next.next == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False