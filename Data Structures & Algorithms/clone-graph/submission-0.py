"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        table = {} # orig: new

        if not node:
            return None
        queue = deque([node])
        while queue:
            length = len(queue)
            for _ in range(length):
                n = queue.pop()
                if n not in table:
                    table[n] = Node(n.val)
                for neighbor in n.neighbors:
                    if neighbor not in table:
                        queue.append(neighbor)

        for orig, copy in table.items():
            for neighbor in orig.neighbors:
                copy.neighbors.append(table[neighbor])
        
        return table[node]
        

        