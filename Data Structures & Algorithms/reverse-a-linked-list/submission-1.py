# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output_head = None

        while head:
            output_head = ListNode(head.val, output_head)
            head = head.next
        
        return output_head