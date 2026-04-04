# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)

                for neighbor in [node.left, node.right]:
                    if neighbor:
                        queue.append(neighbor)
            ans.append(level)
        
        return ans
