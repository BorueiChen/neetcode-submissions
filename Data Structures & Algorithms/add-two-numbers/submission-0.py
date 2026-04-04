# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = 0
        cur = output = ListNode()

        while l1 or l2:
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            cur.next = ListNode(value % 10)
            cur = cur.next
            value = value // 10
        
        if value:
            cur.next = ListNode(value % 10)

        return output.next  