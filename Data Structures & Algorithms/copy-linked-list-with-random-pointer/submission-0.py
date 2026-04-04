"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2Copy = {None: None}

        cur = head
        # build old2copy
        while cur:
            old2Copy[cur] = Node(cur.val)
            cur = cur.next

        # copy next and random
        cur = head
        while cur:
            copy = old2Copy[cur]
            copy.next = old2Copy[cur.next]
            copy.random = old2Copy[cur.random]
            cur = cur.next
        
        return old2Copy[head]