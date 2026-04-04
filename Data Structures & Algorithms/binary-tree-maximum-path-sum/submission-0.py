# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float("-inf")
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, node.val + left + right)
            path = max(left, right)
            if path > 0:
                self.ans = max(self.ans, node.val + path)
                return node.val + path
            else:
                self.ans = max(self.ans, node.val)
                return node.val
        
        dfs(root)
        return self.ans