# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(cur, p, q):
            if (p.val <= cur.val and q.val >= cur.val) or (q.val <= cur.val and p.val >= cur.val):
                return cur
            
            if (p.val < cur.val and q.val < cur.val):
                return dfs(cur.left, p, q)
            else:
                return dfs(cur.right, p, q)
        
        return dfs(root, p, q)