# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None
        
        def dfs(cur):
            if not cur or self.count == k:
                return
            dfs(cur.left)
            self.count += 1
            if self.count == k:
                self.ans = cur.val
                return
            dfs(cur.right)
            return
        
        dfs(root)
        return self.ans