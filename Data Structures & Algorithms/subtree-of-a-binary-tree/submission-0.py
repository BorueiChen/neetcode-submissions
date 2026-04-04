# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(a, b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            
            return (a.val == b.val) and is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

        def dfs(cur, target):
            if not cur:
                return False
            
            res = False
            if cur.val == target.val:
                res = is_same_tree(cur, target)
            
            return res or dfs(cur.left, target) or dfs(cur.right, target)
        
        return dfs(root, subRoot)

        