# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        if root:
            queue = deque()
            queue.append(root)

            while queue:
                length = len(queue)
                for idx in range(length):
                    node = queue.popleft()
                    print(f"{node.val}")
                    if (length - idx) == 1:
                        ans.append(node.val)
                    for neighbor in [node.left, node.right]:
                        if neighbor:
                            print(f"add {neighbor}")
                            queue.append(neighbor)
            
        return ans

