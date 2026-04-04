# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge2lists(a, b):
            cur = head = ListNode()

            while a and b:
                if a.val <= b.val:
                    cur.next = a
                    a = a.next
                else:
                    cur.next = b
                    b = b.next
                cur = cur.next
            
            cur.next = a if a else b
            return head.next
        
        while len(lists) >= 2:
            a = lists.pop()
            b = lists.pop()
            c = merge2lists(a,b)
            lists.append(c)
        
        return lists.pop()
        
        
