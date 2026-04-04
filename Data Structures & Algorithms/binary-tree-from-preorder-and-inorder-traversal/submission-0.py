# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preorder, inorder):
            if len(preorder) == 0:
                return None
            
            val = preorder[0]
            idx = inorder.index(val)

            left_inorder = inorder[:idx]
            right_inorder = inorder[idx+1:] if len(inorder) > 1 else []

            left_preorder = preorder[1:1+len(left_inorder)] if len(preorder) > 1 else []
            right_preorder = preorder[1+len(left_inorder):] if len(preorder) > 1 else []

            node = TreeNode(val)
            node.left = dfs(left_preorder, left_inorder)
            node.right = dfs(right_preorder, right_inorder)

            return node
        
        return dfs(preorder, inorder)